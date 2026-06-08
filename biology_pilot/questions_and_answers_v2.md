# Biology Pilot v2 Questions and Answers

This file is the English readable guide for the recommended biology pilot v2 dataset.

The v2 dataset uses the same 10 biology / biomedical target papers as the earlier draft, but makes three changes:

- Each question includes richer experimental context: model, intervention, comparison group, and readouts.
- There are no `unsupported` answers. Every question corresponds to a relationship studied or supported by the target paper.
- Labels are directional. If an intervention lowers inflammation, tumor growth, cytokine expression, or pathology score, the answer is `negative`, not `positive`.

## Label Meanings

- `positive`: X increases, improves, promotes, or is positively associated with Y.
- `negative`: X decreases, suppresses, reduces, or is negatively associated with Y.
- `null`: the target paper reports no clear effect in this context.
- `mixed`: different readouts move in different directions.

## Dataset Summary

- Target papers: 10
- Questions: 60
- Label distribution: {'positive': 24, 'null': 5, 'mixed': 4, 'negative': 27}
- Question type distribution: {'ordinary': 53, 'null_control': 3, 'context_shift': 4}

## bio_001_inulin_colitis

Target paper: *Inulin aggravates colitis through gut microbiota modulation and MyD88/IL-18 signaling*
PMID: 41133791

1. **bio_001_v2_q01**
   - Question: What is the direction of the effect of `inulin supplementation` on `DSS-induced intestinal inflammation severity`?
   - Relation: `changes`
   - Context: Male C57BL/6 mice were fed a compositionally defined diet supplemented with inulin before or during 2.5% DSS exposure; inflammation was assessed using body-weight trajectory, colon length/weight, histopathology, goblet-cell depletion, fecal lipocalin-2, and colonic cytokine readouts compared with cellulose/control diet.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

2. **bio_001_v2_q02**
   - Question: What is the direction of the effect of `inulin supplementation` on `baseline intestinal inflammation`?
   - Relation: `changes`
   - Context: Steady-state mice received inulin-containing diet without DSS challenge; the comparison asks whether inulin alone induced colitis-like inflammation before chemical injury, using colon pathology and inflammatory readouts rather than DSS-induced disease severity.
   - Question type: `null_control`
   - Gold answer: `null`
   - Gold strength: `unknown`
   - Answer meaning: The target paper reports no clear effect or no detectable change in this context.

3. **bio_001_v2_q03**
   - Question: What is the direction of the effect of `inulin supplementation` on `fecal bacterial load and pro-inflammatory flagellin activity`?
   - Relation: `changes`
   - Context: Fecal microbiota from DSS-treated mice was profiled by 16S sequencing, qPCR-based bacterial-load measurement, and HEK-TLR5 flagellin activity assay; the question asks whether inulin increased microbial signals capable of driving innate inflammatory pathways.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_001_v2_q04**
   - Question: What is the direction of the effect of `inulin supplementation` on `gut microbiota composition`?
   - Relation: `changes`
   - Context: Before and after DSS exposure, fecal bacterial communities were compared by alpha diversity, phylum-level shifts, and genus-level differential abundance; the expected finding is not a single uniform increase or decrease, but a compositional rearrangement with enriched and depleted taxa.
   - Question type: `ordinary`
   - Gold answer: `mixed`
   - Gold strength: `moderate`
   - Answer meaning: Different readouts move in different directions, so the result cannot be summarized as a single positive or negative direction.

5. **bio_001_v2_q05**
   - Question: What is the direction of the effect of `inulin supplementation` on `microbial diversity in offspring or DSS-associated microbiota`?
   - Relation: `changes`
   - Context: Microbial diversity was measured using sequence-based diversity metrics after maternal or direct inulin exposure; the target finding emphasizes loss of diversity in the disease-relevant microbiota context rather than a general prebiotic benefit.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

6. **bio_001_v2_q06**
   - Question: What is the direction of the effect of `antibiotic microbiota depletion or IL-18/MyD88 pathway disruption` on `inulin-exacerbated DSS colitis severity`?
   - Relation: `changes`
   - Context: Inulin-fed DSS-treated mice were tested under microbiota-depleted, MyD88-deficient, TLR5/NLRC4-deficient, or IL-18-deficient conditions; the question asks whether removing microbial or inflammasome signaling reduces the extra colitis severity caused by inulin.
   - Question type: `context_shift`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

## bio_002_btla_asthma

Target paper: *BTLA agonist attenuates Th17-driven inflammation in a mouse model of steroid-resistant asthma*
PMID: 40226621

1. **bio_002_v2_q01**
   - Question: What is the direction of the effect of `BTLA agonist treatment` on `airway hyperreactivity`?
   - Relation: `changes`
   - Context: BXD75 mice were challenged with house-dust-mite allergen and treated with a BTLA agonist during the challenge period; lung resistance after methacholine challenge was used as a functional airway-hyperreactivity readout.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

2. **bio_002_v2_q02**
   - Question: What is the direction of the effect of `BTLA agonist treatment` on `lung inflammation in steroid-resistant asthma`?
   - Relation: `changes`
   - Context: The intervention was evaluated in HDM-challenged BXD75 mice, a strain characterized by neutrophil-skewed steroid-resistant inflammation and elevated Th17 cells; airway and lung inflammation were measured after in vivo agonist treatment.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

3. **bio_002_v2_q03**
   - Question: What is the direction of the effect of `BTLA agonist treatment` on `IL-17 levels from Th17 cells`?
   - Relation: `changes`
   - Context: Th17 cells were treated ex vivo with BTLA agonist, and downstream inflammatory output was evaluated through cell number, inhibitory signaling, NF-kB activity, and IL-17 production.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

4. **bio_002_v2_q04**
   - Question: What is the direction of the effect of `BTLA agonist treatment` on `canonical and non-canonical NF-kB signaling in Th17 cells`?
   - Relation: `changes`
   - Context: RNA-seq and ex vivo Th17-cell assays were used to test whether BTLA agonism shifts inflammatory signaling pathways in steroid-resistant asthma-associated T cells.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

5. **bio_002_v2_q05**
   - Question: What is the direction of the effect of `HDM challenge in BXD75 mice` on `BTLA/HVEM immune-checkpoint expression pattern in lung CD4-positive T cells`?
   - Relation: `changes`
   - Context: Among 58 HDM-exposed murine strains, BXD75 was selected for steroid-resistant asthma features; transcriptomic analysis compared inhibitory BTLA and stimulatory HVEM pathway expression in lung CD4-positive T cells.
   - Question type: `ordinary`
   - Gold answer: `mixed`
   - Gold strength: `moderate`
   - Answer meaning: Different readouts move in different directions, so the result cannot be summarized as a single positive or negative direction.

6. **bio_002_v2_q06**
   - Question: What is the direction of the effect of `BTLA agonist treatment` on `SHP-1-associated inhibitory signaling in Th17 cells`?
   - Relation: `changes`
   - Context: Ex vivo Th17-cell treatment was used to test whether activating BTLA induces inhibitory signaling mechanisms that could explain reduced inflammatory output in steroid-resistant asthma.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

## bio_003_intestinimonas_metabolic

Target paper: *Gut bacterium Intestinimonas butyriciproducens improves host metabolic health: evidence from cohort and animal intervention studies*
PMID: 39833973

1. **bio_003_v2_q01**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens abundance or administration` on `host metabolic health`?
   - Relation: `changes`
   - Context: The target paper combines a human cohort analysis with diet-induced obesity mouse intervention experiments; the question asks whether the bacterium is linked to or causally improves metabolic-health phenotypes rather than merely being taxonomically present.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

2. **bio_003_v2_q02**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens administration` on `blood glucose during insulin tolerance testing`?
   - Relation: `changes`
   - Context: Diet-induced obese mice received the bacterium or placebo; blood glucose during insulin tolerance testing was used to assess insulin sensitivity, with lower glucose after insulin challenge indicating improved insulin responsiveness.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

3. **bio_003_v2_q03**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens administration` on `inguinal white adipose tissue inflammation`?
   - Relation: `changes`
   - Context: In diet-induced obese mice, inguinal white adipose tissue was analyzed after bacterial intervention to test whether inflammatory signatures in adipose tissue were reduced relative to placebo controls.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

4. **bio_003_v2_q04**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens administration` on `adipose browning pathway activity`?
   - Relation: `changes`
   - Context: Inguinal white adipose tissue from diet-induced obese mice was profiled for browning-related pathways after bacterial treatment, asking whether the intervention activates thermogenic or beige-fat-like molecular signatures.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

5. **bio_003_v2_q05**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens administration` on `insulin signaling pathway activity`?
   - Relation: `changes`
   - Context: The intervention was evaluated in diet-induced obese mice, with metabolic tissues analyzed for pathways linked to insulin responsiveness and glucose metabolism after bacterial supplementation.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

6. **bio_003_v2_q06**
   - Question: What is the direction of the effect of `Intestinimonas butyriciproducens administration` on `adiposity in diet-induced obese mice`?
   - Relation: `changes`
   - Context: Diet-induced obese mice were treated with the bacterium or placebo; adiposity and metabolic outcomes were assessed to determine whether the bacterium counteracts obesity-associated fat accumulation.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

## bio_004_crispr_colon

Target paper: *A Novel CRISPR/Cas9-mediated Mouse Model of Colon Carcinogenesis*
PMID: 39128652

1. **bio_004_v2_q01**
   - Question: What is the direction of the effect of `dox-inducible multiplexed CRISPR/Cas9 mutagenesis` on `sporadic colorectal tumor formation`?
   - Relation: `changes`
   - Context: Mouse colon epithelium was engineered for inducible Cas9 nickase activity with guide RNAs targeting common colorectal cancer genes including Apc, Pten, Trp53, and Smad4; tumor formation was evaluated after dox induction.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

2. **bio_004_v2_q02**
   - Question: What is the direction of the effect of `longer dox induction of the CRISPR/Cas9 system` on `number of colon tumors per mouse`?
   - Relation: `changes`
   - Context: The inducible system allowed comparison of different dox-exposure durations; tumor counts were used to test whether longer mutagenesis exposure increases colon tumor initiation in the engineered model.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

3. **bio_004_v2_q03**
   - Question: What is the direction of the effect of `gut-specific PLAGL2 overexpression` on `colon tumor growth`?
   - Relation: `changes`
   - Context: The CRISPR/Cas9-mediated colon carcinogenesis model was used to validate PLAGL2 as a candidate driver; tumor growth was compared between PLAGL2-overexpressing and control settings.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_004_v2_q04**
   - Question: What is the direction of the effect of `somatic inactivation of Apc, Pten, Trp53, and Smad4` on `multi-step colorectal cancer pathogenesis modeling capacity`?
   - Relation: `changes`
   - Context: Multiple tumor-suppressor and pathway genes commonly altered in human colorectal cancer were targeted in the colon epithelium to test whether the model recapitulates staged CRC-like genetic pathogenesis.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

5. **bio_004_v2_q05**
   - Question: What is the direction of the effect of `dox-inactivatable repressor co-expression` on `leaky CRISPR activity before dox induction`?
   - Relation: `changes`
   - Context: The engineering strategy included regulatory elements to control Cas9 activity; leakiness was tested before induction to determine whether the repressor lowers background editing activity in the model system.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

6. **bio_004_v2_q06**
   - Question: What is the direction of the effect of `the inducible CRISPR/Cas9 colon model` on `need for Cre-mediated recombination to initiate somatic mutations`?
   - Relation: `changes`
   - Context: The model was designed as a dox-inducible CRISPR/Cas9 mutagenesis system rather than a classic Cre-lox conditional allele model; the question asks whether this design reduces reliance on Cre recombinase as the initiating mutational mechanism.
   - Question type: `context_shift`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

## bio_005_mwa_ici

Target paper: *Microwave ablation combined with immune checkpoint inhibitor enhanced the antitumor immune activation and memory in rechallenged tumor mouse model*
PMID: 40131498

1. **bio_005_v2_q01**
   - Question: What is the direction of the effect of `microwave ablation combined with immune checkpoint inhibitor` on `rechallenged tumor growth`?
   - Relation: `changes`
   - Context: A post-ablation tumor rechallenge mouse model was used to test whether combining microwave ablation with checkpoint blockade controls growth of newly challenged tumors better than monotherapy or control conditions.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

2. **bio_005_v2_q02**
   - Question: What is the direction of the effect of `microwave ablation monotherapy` on `rechallenged tumor growth`?
   - Relation: `changes`
   - Context: The same rechallenge model separated microwave ablation alone from the combination arm to determine whether ablation by itself was sufficient to suppress subsequent tumor growth.
   - Question type: `null_control`
   - Gold answer: `null`
   - Gold strength: `unknown`
   - Answer meaning: The target paper reports no clear effect or no detectable change in this context.

3. **bio_005_v2_q03**
   - Question: What is the direction of the effect of `microwave ablation monotherapy` on `PD-L1 expression on tumor cells`?
   - Relation: `changes`
   - Context: Tumor cells after microwave ablation were analyzed for PD-L1 expression to test whether ablation creates a checkpoint-inhibitor-relevant immune escape signal that could motivate combination therapy.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_005_v2_q04**
   - Question: What is the direction of the effect of `microwave ablation combined with immune checkpoint inhibitor` on `antitumor immune activation`?
   - Relation: `changes`
   - Context: Immune-cell phenotypes in tumors and draining lymph nodes were measured after rechallenge to determine whether the combination therapy increased activated antitumor immune populations relative to ablation-only or checkpoint-only conditions.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

5. **bio_005_v2_q05**
   - Question: What is the direction of the effect of `microwave ablation combined with immune checkpoint inhibitor` on `antitumor immune memory`?
   - Relation: `changes`
   - Context: The rechallenge design tested whether prior local ablation plus checkpoint blockade produced memory-like immune protection against later tumor exposure, measured through tumor control and memory-associated immune readouts.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

6. **bio_005_v2_q06**
   - Question: What is the direction of the effect of `microwave ablation plus checkpoint blockade` on `tumor immune microenvironment`?
   - Relation: `changes`
   - Context: The treatment was evaluated across effector activation, checkpoint signaling, and memory-associated immune features; because some antitumor markers increase while tumor burden decreases, the immune microenvironment changes are multidirectional rather than a single scalar shift.
   - Question type: `ordinary`
   - Gold answer: `mixed`
   - Gold strength: `moderate`
   - Answer meaning: Different readouts move in different directions, so the result cannot be summarized as a single positive or negative direction.

## bio_006_uchl5_hnscc

Target paper: *In vivo CRISPR screening in head and neck cancer reveals Uchl5 as an immunotherapy target*
PMID: 41022734

1. **bio_006_v2_q01**
   - Question: What is the direction of the effect of `in vivo CRISPR knockout screening` on `identification of Uchl5 as an immune-evasion gene`?
   - Relation: `changes`
   - Context: A syngeneic head and neck squamous cell carcinoma mouse model was screened in vivo to find tumor-intrinsic genes whose loss changes immune sensitivity and response to immune checkpoint blockade.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

2. **bio_006_v2_q02**
   - Question: What is the direction of the effect of `Uchl5 deficiency` on `CD8-positive T-cell infiltration`?
   - Relation: `changes`
   - Context: Uchl5-deficient HNSCC tumors were evaluated in immunocompetent mice to test whether loss of this deubiquitinating enzyme increases antitumor T-cell entry into the tumor microenvironment.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

3. **bio_006_v2_q03**
   - Question: What is the direction of the effect of `Uchl5 deficiency` on `anti-PD1 treatment response`?
   - Relation: `changes`
   - Context: Orthotopic and syngeneic HNSCC mouse models were used to test whether tumors lacking Uchl5 become more sensitive to anti-PD1 immune checkpoint blockade.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_006_v2_q04**
   - Question: What is the direction of the effect of `Uchl5 deficiency plus anti-PD1 treatment` on `tumor growth in immunocompetent mice`?
   - Relation: `changes`
   - Context: Uchl5-deficient tumor cells were implanted into immunocompetent C57BL/6 mice and treated with anti-PD1; tumor growth was compared with Uchl5-intact controls to assess immune-dependent tumor control.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

5. **bio_006_v2_q05**
   - Question: What is the direction of the effect of `Uchl5 deficiency` on `anti-PD1 response in NSG immunodeficient mice`?
   - Relation: `changes`
   - Context: A context-shift comparison asks whether the benefit of Uchl5 loss persists in NSG mice lacking adaptive immunity; this tests whether the effect depends on an intact antitumor immune system.
   - Question type: `context_shift`
   - Gold answer: `null`
   - Gold strength: `unknown`
   - Answer meaning: The target paper reports no clear effect or no detectable change in this context.

6. **bio_006_v2_q06**
   - Question: What is the direction of the effect of `Uchl5 deficiency` on `survival after immune checkpoint blockade`?
   - Relation: `changes`
   - Context: Mouse HNSCC models were followed after Uchl5 perturbation and checkpoint blockade to determine whether increased immune sensitivity translates into improved survival outcomes.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

## bio_007_fh15_colitis

Target paper: *Fh15 Reduces Colonic Inflammation and Leukocyte Infiltration in a Dextran Sulfate Sodium-Induced Ulcerative Colitis Mouse Model*
PMID: 40497975

1. **bio_007_v2_q01**
   - Question: What is the direction of the effect of `Fh15 treatment` on `disease activity index in DSS-induced ulcerative colitis`?
   - Relation: `changes`
   - Context: Male C57BL/6 mice received 4% DSS in drinking water to induce ulcerative colitis and were treated intraperitoneally with recombinant Fh15 on days 1, 3, and 5; daily DAI integrated body-weight loss, stool consistency, and bleeding severity.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

2. **bio_007_v2_q02**
   - Question: What is the direction of the effect of `Fh15 treatment` on `colon-shortening severity`?
   - Relation: `changes`
   - Context: Colon length was measured after DSS exposure as an indirect marker of inflammation and tissue damage; Fh15-treated DSS mice were compared against DSS-only controls.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

3. **bio_007_v2_q03**
   - Question: What is the direction of the effect of `Fh15 treatment` on `histopathological colitis score`?
   - Relation: `changes`
   - Context: H&E-stained distal colon sections from DSS and DSS+Fh15 groups were scored for inflammatory and tissue-damage changes to assess whether treatment ameliorated microscopic disease severity.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

4. **bio_007_v2_q04**
   - Question: What is the direction of the effect of `Fh15 treatment` on `TNF-alpha and IL-1beta expression in distal colon`?
   - Relation: `changes`
   - Context: RT-PCR was used to measure pro-inflammatory cytokine expression in distal colon tissue from DSS-induced colitis mice treated with Fh15 versus DSS-only controls.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

5. **bio_007_v2_q05**
   - Question: What is the direction of the effect of `Fh15 treatment` on `neutrophil and macrophage infiltration in colon tissue`?
   - Relation: `changes`
   - Context: Immunohistochemistry quantified Ly6G-positive neutrophils and F4/80-positive macrophages in colonic samples from DSS-induced colitis mice with or without Fh15 treatment.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

6. **bio_007_v2_q06**
   - Question: What is the direction of the effect of `Fh15 treatment` on `CD86 expression on spleen CD11b-positive CD11c-negative cells`?
   - Relation: `changes`
   - Context: Flow cytometry of splenocytes from DSS and DSS+Fh15 mice measured CD86 expression within the CD11b-positive CD11c-negative cell population to test whether Fh15 reduces systemic myeloid activation markers.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

## bio_008_cryo_pd1_cervical

Target paper: *Cryoablation synergizes with anti-PD-1 immunotherapy induces an effective abscopal effect in murine model of cervical cancer*
PMID: 39489086

1. **bio_008_v2_q01**
   - Question: What is the direction of the effect of `cryoablation combined with anti-PD-1 antibody` on `distant untreated tumor growth`?
   - Relation: `changes`
   - Context: A murine U14 bilateral subcutaneous cervical cancer model was used: one tumor received local cryoablation while the contralateral tumor was left untreated to measure systemic abscopal tumor control under anti-PD-1 combination therapy.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

2. **bio_008_v2_q02**
   - Question: What is the direction of the effect of `cryoablation combined with anti-PD-1 antibody` on `mouse survival`?
   - Relation: `changes`
   - Context: Survival was followed in cervical-cancer-bearing mice treated with local cryoablation, anti-PD-1 antibody, their combination, or control treatment to determine whether systemic tumor control translated into survival benefit.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

3. **bio_008_v2_q03**
   - Question: What is the direction of the effect of `cryoablation or cryoablation plus anti-PD-1 treatment` on `CD8-positive T-cell infiltration in distant tumors`?
   - Relation: `changes`
   - Context: Distant non-ablated tumors were analyzed after treatment to test whether local cryoablation and checkpoint blockade increase cytotoxic T-cell infiltration at untreated tumor sites.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_008_v2_q04**
   - Question: What is the direction of the effect of `cryoablation combined with anti-PD-1 antibody` on `M2-like tumor-associated macrophages and myeloid-derived suppressor cells`?
   - Relation: `changes`
   - Context: Immune profiling of distant tumors tested whether the combination therapy reduces immunosuppressive myeloid populations while promoting a more antitumor immune microenvironment.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

5. **bio_008_v2_q05**
   - Question: What is the direction of the effect of `anti-PD-1 antibody monotherapy without cryoablation` on `strong abscopal tumor control`?
   - Relation: `changes`
   - Context: The bilateral cervical cancer model included anti-PD-1 treatment without local cryoablation; this context tests whether checkpoint blockade alone generated the strong systemic abscopal effect seen with the combination.
   - Question type: `context_shift`
   - Gold answer: `null`
   - Gold strength: `unknown`
   - Answer meaning: The target paper reports no clear effect or no detectable change in this context.

6. **bio_008_v2_q06**
   - Question: What is the direction of the effect of `cryoablation combined with anti-PD-1 antibody` on `overall distant-tumor immune microenvironment`?
   - Relation: `changes`
   - Context: The target paper measured both effector immune features and suppressive cell populations in distant tumors; the combined therapy is expected to increase antitumor cells while decreasing suppressive myeloid populations.
   - Question type: `ordinary`
   - Gold answer: `mixed`
   - Gold strength: `moderate`
   - Answer meaning: Different readouts move in different directions, so the result cannot be summarized as a single positive or negative direction.

## bio_009_gastric_crispr

Target paper: *Gastric Organoid-Based Ectopic and Orthotopic In Vivo CRISPR Screening for Tumor Suppressors in Gastric Cancer*
PMID: 41288537

1. **bio_009_v2_q01**
   - Question: What is the direction of the effect of `Pten inactivation` on `gastric tumor size`?
   - Relation: `changes`
   - Context: Gastric organoid-based ectopic and orthotopic in vivo CRISPR screens perturbed candidate tumor suppressors; tumors with Pten inactivation were compared with other genotypes to assess growth-promoting effects.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `strong`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

2. **bio_009_v2_q02**
   - Question: What is the direction of the effect of `Pten inactivation` on `neo-angiogenesis in large gastric tumors`?
   - Relation: `changes`
   - Context: Large gastric tumors generated through organoid-based CRISPR perturbation were analyzed for vascular or angiogenic features to test whether Pten loss promotes a more angiogenic tumor phenotype.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

3. **bio_009_v2_q03**
   - Question: What is the direction of the effect of `Pten inactivation` on `neutrophil recruitment and T-cell exclusion`?
   - Relation: `changes`
   - Context: The tumor immune microenvironment in Pten-inactivated gastric tumors was profiled to assess whether loss of Pten is associated with neutrophil-rich and T-cell-excluded immune architecture.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

4. **bio_009_v2_q04**
   - Question: What is the direction of the effect of `Smad4, Tgfbr1, or Acvr2a inactivation` on `intestinal metaplasia and compensatory hyperplasia-like phenotypes`?
   - Relation: `changes`
   - Context: Specific TGF-beta pathway-related tumor suppressor perturbations were evaluated in gastric organoid-derived tumors to determine whether they produce gastric epithelial phenotypes resembling intestinal metaplasia or compensatory hyperplasia.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

5. **bio_009_v2_q05**
   - Question: What is the direction of the effect of `Helicobacter pylori infection` on `tumor mutational landscape`?
   - Relation: `changes`
   - Context: The CRISPR gastric tumor models were studied in the presence or absence of H. pylori to test whether the pathogen altered tumor genetics directly rather than mainly reshaping the tumor microenvironment.
   - Question type: `null_control`
   - Gold answer: `null`
   - Gold strength: `unknown`
   - Answer meaning: The target paper reports no clear effect or no detectable change in this context.

6. **bio_009_v2_q06**
   - Question: What is the direction of the effect of `Helicobacter pylori infection` on `tumor-promoting SiglecF-positive neutrophil recruitment`?
   - Relation: `changes`
   - Context: The gastric tumor microenvironment was profiled after H. pylori exposure to test whether infection recruits a neutrophil population with tumor-promoting features rather than altering only tumor-cell genotype.
   - Question type: `ordinary`
   - Gold answer: `positive`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention increases, improves, promotes, or is positively associated with the outcome.

## bio_010_if_colitis

Target paper: *Intermittent Fasting Reduces Intestinal Inflammation in Dextran Sulfate Sodium-Induced Colitis of Mice*
PMID: 39898122

1. **bio_010_v2_q01**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `intestinal inflammation in DSS-induced colitis`?
   - Relation: `changes`
   - Context: Mice underwent repeated DSS-induced colitis cycles, and intermittent fasting was applied during later cycles; intestinal inflammation was evaluated using disease signs, colon morphology, histology, and immune-cell readouts.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

2. **bio_010_v2_q02**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `disease activity index or visible colitis symptoms`?
   - Relation: `changes`
   - Context: During chronic DSS cycles, DAI components such as occult blood, stool changes, and body-weight loss were monitored to test whether intermittent fasting reduced clinical disease severity compared with DSS controls.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

3. **bio_010_v2_q03**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `DSS-mediated colon-shortening severity`?
   - Relation: `changes`
   - Context: Colon length was measured after repeated DSS exposure to test whether fasting mitigated the structural shortening associated with chronic colitis injury.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

4. **bio_010_v2_q04**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `colonic histological injury score`?
   - Relation: `changes`
   - Context: Colon sections were scored on a 0-4 histological scale covering mucosal inflammation, edema, and crypt injury after DSS with or without intermittent fasting intervention.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

5. **bio_010_v2_q05**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `CD4-positive T-cell proportion in spleen and mesenteric lymph nodes`?
   - Relation: `changes`
   - Context: Immune-cell populations in systemic and gut-draining lymphoid tissues were profiled after DSS colitis and fasting intervention to evaluate whether adaptive immune-cell proportions changed with reduced inflammation.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

6. **bio_010_v2_q06**
   - Question: What is the direction of the effect of `intermittent fasting intervention` on `macrophage infiltration around the crypt base`?
   - Relation: `changes`
   - Context: Colonic immune infiltration was assessed around crypt-base regions after DSS-induced injury to test whether fasting reduced macrophage accumulation associated with intestinal inflammation.
   - Question type: `ordinary`
   - Gold answer: `negative`
   - Gold strength: `moderate`
   - Answer meaning: The variable or intervention decreases, suppresses, reduces, or is negatively associated with the outcome.

