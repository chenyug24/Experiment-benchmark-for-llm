from __future__ import annotations

import argparse
import json
from pathlib import Path

from .baselines import (
    evidence_voting_baseline,
    majority_baseline,
    nearest_prior_paper_baseline,
    random_baseline,
)
from .io import load_corpus, load_instances, write_jsonl, write_predictions
from .metrics import metric_report
from .search_gate import gate_search_results
from .temporal import allowed_prior_papers, cutoff_date, leakage_flags


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Temporal scientific finding benchmark CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate instances, corpus, and leakage rules.")
    validate_parser.add_argument("--instances", required=True)
    validate_parser.add_argument("--corpus", required=True)
    validate_parser.add_argument("--access-mode", default="preprint_aware", choices=["strict", "preprint_aware", "reference_only"])

    run_parser = subparsers.add_parser("run-baseline", help="Run a deterministic baseline.")
    run_parser.add_argument("--instances", required=True)
    run_parser.add_argument("--corpus", required=True)
    run_parser.add_argument("--train-instances")
    run_parser.add_argument("--baseline", required=True, choices=["majority", "random", "nearest", "vote", "weighted_vote"])
    run_parser.add_argument("--access-mode", default="preprint_aware", choices=["strict", "preprint_aware", "reference_only"])
    run_parser.add_argument("--k", type=int, default=5)
    run_parser.add_argument("--seed", type=int, default=7)
    run_parser.add_argument("--out", required=True)

    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate prediction JSONL against benchmark instances.")
    evaluate_parser.add_argument("--instances", required=True)
    evaluate_parser.add_argument("--predictions", required=True)

    gate_parser = subparsers.add_parser(
        "gate-search",
        help="Filter agent/search candidate papers through cutoff and leakage rules.",
    )
    gate_parser.add_argument("--instances", required=True)
    gate_parser.add_argument("--candidate-corpus", required=True)
    gate_parser.add_argument("--access-mode", default="preprint_aware", choices=["strict", "preprint_aware", "reference_only"])
    gate_parser.add_argument("--out", required=True)
    gate_parser.add_argument("--audit-out", required=True)

    args = parser.parse_args(argv)
    if args.command == "validate":
        _validate(args.instances, args.corpus, args.access_mode)
    elif args.command == "run-baseline":
        _run_baseline(args)
    elif args.command == "evaluate":
        _evaluate(args.instances, args.predictions)
    elif args.command == "gate-search":
        _gate_search(args)


def _validate(instance_path: str, corpus_path: str, access_mode: str) -> None:
    instances = load_instances(instance_path)
    corpus = load_corpus(corpus_path)
    total_allowed = 0
    all_flags: dict[str, list[str]] = {}
    for instance in instances:
        allowed = allowed_prior_papers(instance, corpus, access_mode=access_mode)
        total_allowed += len(allowed)
        flags = leakage_flags(instance, corpus)
        if flags:
            all_flags[instance.instance_id] = flags
        cutoff = cutoff_date(instance.target_paper.release_dates, instance.target_paper.buffer_days)
        print(f"{instance.instance_id}: cutoff={cutoff} allowed_prior_papers={len(allowed)}")
    if all_flags:
        print("\nLeakage warnings:")
        for instance_id, flags in all_flags.items():
            for flag in flags:
                print(f"- {instance_id}: {flag}")
    print(f"\nValidated {len(instances)} instances against {len(corpus)} corpus papers.")
    print(f"Mean allowed prior papers: {total_allowed / len(instances):.2f}" if instances else "No instances.")


def _run_baseline(args: argparse.Namespace) -> None:
    instances = load_instances(args.instances)
    corpus = load_corpus(args.corpus)
    if args.baseline == "majority":
        train_path = args.train_instances or args.instances
        train_instances = load_instances(train_path)
        predictions = majority_baseline(train_instances, instances)
    elif args.baseline == "random":
        predictions = random_baseline(instances, seed=args.seed)
    elif args.baseline == "nearest":
        predictions = nearest_prior_paper_baseline(instances, corpus, access_mode=args.access_mode)
    elif args.baseline == "vote":
        predictions = evidence_voting_baseline(instances, corpus, access_mode=args.access_mode, k=args.k, weighted=False)
    elif args.baseline == "weighted_vote":
        predictions = evidence_voting_baseline(instances, corpus, access_mode=args.access_mode, k=args.k, weighted=True)
    else:
        raise ValueError(f"Unsupported baseline: {args.baseline}")
    write_predictions(args.out, predictions)
    report = metric_report(instances, predictions)
    print(json.dumps(report, indent=2, sort_keys=True))
    print(f"Wrote predictions to {Path(args.out)}")


def _evaluate(instance_path: str, prediction_path: str) -> None:
    from .io import load_predictions

    instances = load_instances(instance_path)
    predictions = load_predictions(prediction_path)
    print(json.dumps(metric_report(instances, predictions), indent=2, sort_keys=True))


def _gate_search(args: argparse.Namespace) -> None:
    instances = load_instances(args.instances)
    candidates = load_corpus(args.candidate_corpus)
    allowed_corpus, audit_records = gate_search_results(instances, candidates, access_mode=args.access_mode)
    write_jsonl(args.out, (paper.to_dict() for paper in allowed_corpus))
    write_jsonl(args.audit_out, (record.to_dict() for record in audit_records))

    rejected = sum(1 for record in audit_records if record.decision == "rejected")
    allowed = sum(1 for record in audit_records if record.decision == "allowed")
    report = {
        "instances": len(instances),
        "candidate_papers": len(candidates),
        "deduped_allowed_corpus_papers": len(allowed_corpus),
        "allowed_instance_candidate_pairs": allowed,
        "rejected_instance_candidate_pairs": rejected,
        "access_mode": args.access_mode,
        "out": str(Path(args.out)),
        "audit_out": str(Path(args.audit_out)),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
