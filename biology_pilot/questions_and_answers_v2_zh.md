# Biology Pilot v2 问题与答案

这版使用之前的 10 篇 biology / biomedical target papers，但修正了三个问题：

- 每个问题给更完整的实验 context，包括模型、处理组、对照和主要 readouts。
- 不再使用 `unsupported` 答案；所有问题都对应 target paper 中实际研究或可被结果支持的关系。
- 不再把所有被支持的关系都标为 `positive`；如果 intervention 降低炎症、肿瘤生长、细胞因子或病理评分，则标为 `negative`。

标签含义：

- `positive`: X 增加 Y、促进 Y、提高 Y，或与 Y 正相关。
- `negative`: X 降低 Y、抑制 Y、减少 Y，或与 Y 负相关。
- `null`: target paper 中该 context 下没有检测到明显改变。
- `mixed`: 同一关系下多个 readouts 方向不一致，例如一些免疫指标上升、另一些下降。

总题数：60

答案分布：{'positive': 24, 'null': 5, 'mixed': 4, 'negative': 27}

问题类型分布：{'ordinary': 53, 'null_control': 3, 'context_shift': 4}

## bio_001_inulin_colitis

Target paper: *Inulin aggravates colitis through gut microbiota modulation and MyD88/IL-18 signaling*
PMID: 41133791

1. **bio_001_v2_q01**
   - 问题：`inulin supplementation` 对 `DSS-induced intestinal inflammation severity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Male C57BL/6 mice were fed a compositionally defined diet supplemented with inulin before or during 2.5% DSS exposure; inflammation was assessed using body-weight trajectory, colon length/weight, histopathology, goblet-cell depletion, fecal lipocalin-2, and colonic cytokine readouts compared with cellulose/control diet.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 增加、增强或改善。

2. **bio_001_v2_q02**
   - 问题：`inulin supplementation` 对 `baseline intestinal inflammation` 的影响方向是什么？
   - Relation: `changes`
   - Context: Steady-state mice received inulin-containing diet without DSS challenge; the comparison asks whether inulin alone induced colitis-like inflammation before chemical injury, using colon pathology and inflammatory readouts rather than DSS-induced disease severity.
   - 类型：`null_control`
   - 答案：`null`
   - 强度：`unknown`
   - 答案含义：在这个 context 下，target paper 没有显示明显改变。

3. **bio_001_v2_q03**
   - 问题：`inulin supplementation` 对 `fecal bacterial load and pro-inflammatory flagellin activity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Fecal microbiota from DSS-treated mice was profiled by 16S sequencing, qPCR-based bacterial-load measurement, and HEK-TLR5 flagellin activity assay; the question asks whether inulin increased microbial signals capable of driving innate inflammatory pathways.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_001_v2_q04**
   - 问题：`inulin supplementation` 对 `gut microbiota composition` 的影响方向是什么？
   - Relation: `changes`
   - Context: Before and after DSS exposure, fecal bacterial communities were compared by alpha diversity, phylum-level shifts, and genus-level differential abundance; the expected finding is not a single uniform increase or decrease, but a compositional rearrangement with enriched and depleted taxa.
   - 类型：`ordinary`
   - 答案：`mixed`
   - 强度：`moderate`
   - 答案含义：多个 readouts 方向不同，不能用单一正/负方向概括。

5. **bio_001_v2_q05**
   - 问题：`inulin supplementation` 对 `microbial diversity in offspring or DSS-associated microbiota` 的影响方向是什么？
   - Relation: `changes`
   - Context: Microbial diversity was measured using sequence-based diversity metrics after maternal or direct inulin exposure; the target finding emphasizes loss of diversity in the disease-relevant microbiota context rather than a general prebiotic benefit.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

6. **bio_001_v2_q06**
   - 问题：`antibiotic microbiota depletion or IL-18/MyD88 pathway disruption` 对 `inulin-exacerbated DSS colitis severity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Inulin-fed DSS-treated mice were tested under microbiota-depleted, MyD88-deficient, TLR5/NLRC4-deficient, or IL-18-deficient conditions; the question asks whether removing microbial or inflammasome signaling reduces the extra colitis severity caused by inulin.
   - 类型：`context_shift`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

## bio_002_btla_asthma

Target paper: *BTLA agonist attenuates Th17-driven inflammation in a mouse model of steroid-resistant asthma*
PMID: 40226621

1. **bio_002_v2_q01**
   - 问题：`BTLA agonist treatment` 对 `airway hyperreactivity` 的影响方向是什么？
   - Relation: `changes`
   - Context: BXD75 mice were challenged with house-dust-mite allergen and treated with a BTLA agonist during the challenge period; lung resistance after methacholine challenge was used as a functional airway-hyperreactivity readout.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

2. **bio_002_v2_q02**
   - 问题：`BTLA agonist treatment` 对 `lung inflammation in steroid-resistant asthma` 的影响方向是什么？
   - Relation: `changes`
   - Context: The intervention was evaluated in HDM-challenged BXD75 mice, a strain characterized by neutrophil-skewed steroid-resistant inflammation and elevated Th17 cells; airway and lung inflammation were measured after in vivo agonist treatment.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

3. **bio_002_v2_q03**
   - 问题：`BTLA agonist treatment` 对 `IL-17 levels from Th17 cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Th17 cells were treated ex vivo with BTLA agonist, and downstream inflammatory output was evaluated through cell number, inhibitory signaling, NF-kB activity, and IL-17 production.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

4. **bio_002_v2_q04**
   - 问题：`BTLA agonist treatment` 对 `canonical and non-canonical NF-kB signaling in Th17 cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: RNA-seq and ex vivo Th17-cell assays were used to test whether BTLA agonism shifts inflammatory signaling pathways in steroid-resistant asthma-associated T cells.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

5. **bio_002_v2_q05**
   - 问题：`HDM challenge in BXD75 mice` 对 `BTLA/HVEM immune-checkpoint expression pattern in lung CD4-positive T cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Among 58 HDM-exposed murine strains, BXD75 was selected for steroid-resistant asthma features; transcriptomic analysis compared inhibitory BTLA and stimulatory HVEM pathway expression in lung CD4-positive T cells.
   - 类型：`ordinary`
   - 答案：`mixed`
   - 强度：`moderate`
   - 答案含义：多个 readouts 方向不同，不能用单一正/负方向概括。

6. **bio_002_v2_q06**
   - 问题：`BTLA agonist treatment` 对 `SHP-1-associated inhibitory signaling in Th17 cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Ex vivo Th17-cell treatment was used to test whether activating BTLA induces inhibitory signaling mechanisms that could explain reduced inflammatory output in steroid-resistant asthma.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

## bio_003_intestinimonas_metabolic

Target paper: *Gut bacterium Intestinimonas butyriciproducens improves host metabolic health: evidence from cohort and animal intervention studies*
PMID: 39833973

1. **bio_003_v2_q01**
   - 问题：`Intestinimonas butyriciproducens abundance or administration` 对 `host metabolic health` 的影响方向是什么？
   - Relation: `changes`
   - Context: The target paper combines a human cohort analysis with diet-induced obesity mouse intervention experiments; the question asks whether the bacterium is linked to or causally improves metabolic-health phenotypes rather than merely being taxonomically present.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

2. **bio_003_v2_q02**
   - 问题：`Intestinimonas butyriciproducens administration` 对 `blood glucose during insulin tolerance testing` 的影响方向是什么？
   - Relation: `changes`
   - Context: Diet-induced obese mice received the bacterium or placebo; blood glucose during insulin tolerance testing was used to assess insulin sensitivity, with lower glucose after insulin challenge indicating improved insulin responsiveness.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

3. **bio_003_v2_q03**
   - 问题：`Intestinimonas butyriciproducens administration` 对 `inguinal white adipose tissue inflammation` 的影响方向是什么？
   - Relation: `changes`
   - Context: In diet-induced obese mice, inguinal white adipose tissue was analyzed after bacterial intervention to test whether inflammatory signatures in adipose tissue were reduced relative to placebo controls.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

4. **bio_003_v2_q04**
   - 问题：`Intestinimonas butyriciproducens administration` 对 `adipose browning pathway activity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Inguinal white adipose tissue from diet-induced obese mice was profiled for browning-related pathways after bacterial treatment, asking whether the intervention activates thermogenic or beige-fat-like molecular signatures.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

5. **bio_003_v2_q05**
   - 问题：`Intestinimonas butyriciproducens administration` 对 `insulin signaling pathway activity` 的影响方向是什么？
   - Relation: `changes`
   - Context: The intervention was evaluated in diet-induced obese mice, with metabolic tissues analyzed for pathways linked to insulin responsiveness and glucose metabolism after bacterial supplementation.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

6. **bio_003_v2_q06**
   - 问题：`Intestinimonas butyriciproducens administration` 对 `adiposity in diet-induced obese mice` 的影响方向是什么？
   - Relation: `changes`
   - Context: Diet-induced obese mice were treated with the bacterium or placebo; adiposity and metabolic outcomes were assessed to determine whether the bacterium counteracts obesity-associated fat accumulation.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

## bio_004_crispr_colon

Target paper: *A Novel CRISPR/Cas9-mediated Mouse Model of Colon Carcinogenesis*
PMID: 39128652

1. **bio_004_v2_q01**
   - 问题：`dox-inducible multiplexed CRISPR/Cas9 mutagenesis` 对 `sporadic colorectal tumor formation` 的影响方向是什么？
   - Relation: `changes`
   - Context: Mouse colon epithelium was engineered for inducible Cas9 nickase activity with guide RNAs targeting common colorectal cancer genes including Apc, Pten, Trp53, and Smad4; tumor formation was evaluated after dox induction.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 增加、增强或改善。

2. **bio_004_v2_q02**
   - 问题：`longer dox induction of the CRISPR/Cas9 system` 对 `number of colon tumors per mouse` 的影响方向是什么？
   - Relation: `changes`
   - Context: The inducible system allowed comparison of different dox-exposure durations; tumor counts were used to test whether longer mutagenesis exposure increases colon tumor initiation in the engineered model.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

3. **bio_004_v2_q03**
   - 问题：`gut-specific PLAGL2 overexpression` 对 `colon tumor growth` 的影响方向是什么？
   - Relation: `changes`
   - Context: The CRISPR/Cas9-mediated colon carcinogenesis model was used to validate PLAGL2 as a candidate driver; tumor growth was compared between PLAGL2-overexpressing and control settings.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_004_v2_q04**
   - 问题：`somatic inactivation of Apc, Pten, Trp53, and Smad4` 对 `multi-step colorectal cancer pathogenesis modeling capacity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Multiple tumor-suppressor and pathway genes commonly altered in human colorectal cancer were targeted in the colon epithelium to test whether the model recapitulates staged CRC-like genetic pathogenesis.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

5. **bio_004_v2_q05**
   - 问题：`dox-inactivatable repressor co-expression` 对 `leaky CRISPR activity before dox induction` 的影响方向是什么？
   - Relation: `changes`
   - Context: The engineering strategy included regulatory elements to control Cas9 activity; leakiness was tested before induction to determine whether the repressor lowers background editing activity in the model system.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

6. **bio_004_v2_q06**
   - 问题：`the inducible CRISPR/Cas9 colon model` 对 `need for Cre-mediated recombination to initiate somatic mutations` 的影响方向是什么？
   - Relation: `changes`
   - Context: The model was designed as a dox-inducible CRISPR/Cas9 mutagenesis system rather than a classic Cre-lox conditional allele model; the question asks whether this design reduces reliance on Cre recombinase as the initiating mutational mechanism.
   - 类型：`context_shift`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

## bio_005_mwa_ici

Target paper: *Microwave ablation combined with immune checkpoint inhibitor enhanced the antitumor immune activation and memory in rechallenged tumor mouse model*
PMID: 40131498

1. **bio_005_v2_q01**
   - 问题：`microwave ablation combined with immune checkpoint inhibitor` 对 `rechallenged tumor growth` 的影响方向是什么？
   - Relation: `changes`
   - Context: A post-ablation tumor rechallenge mouse model was used to test whether combining microwave ablation with checkpoint blockade controls growth of newly challenged tumors better than monotherapy or control conditions.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

2. **bio_005_v2_q02**
   - 问题：`microwave ablation monotherapy` 对 `rechallenged tumor growth` 的影响方向是什么？
   - Relation: `changes`
   - Context: The same rechallenge model separated microwave ablation alone from the combination arm to determine whether ablation by itself was sufficient to suppress subsequent tumor growth.
   - 类型：`null_control`
   - 答案：`null`
   - 强度：`unknown`
   - 答案含义：在这个 context 下，target paper 没有显示明显改变。

3. **bio_005_v2_q03**
   - 问题：`microwave ablation monotherapy` 对 `PD-L1 expression on tumor cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Tumor cells after microwave ablation were analyzed for PD-L1 expression to test whether ablation creates a checkpoint-inhibitor-relevant immune escape signal that could motivate combination therapy.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_005_v2_q04**
   - 问题：`microwave ablation combined with immune checkpoint inhibitor` 对 `antitumor immune activation` 的影响方向是什么？
   - Relation: `changes`
   - Context: Immune-cell phenotypes in tumors and draining lymph nodes were measured after rechallenge to determine whether the combination therapy increased activated antitumor immune populations relative to ablation-only or checkpoint-only conditions.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

5. **bio_005_v2_q05**
   - 问题：`microwave ablation combined with immune checkpoint inhibitor` 对 `antitumor immune memory` 的影响方向是什么？
   - Relation: `changes`
   - Context: The rechallenge design tested whether prior local ablation plus checkpoint blockade produced memory-like immune protection against later tumor exposure, measured through tumor control and memory-associated immune readouts.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

6. **bio_005_v2_q06**
   - 问题：`microwave ablation plus checkpoint blockade` 对 `tumor immune microenvironment` 的影响方向是什么？
   - Relation: `changes`
   - Context: The treatment was evaluated across effector activation, checkpoint signaling, and memory-associated immune features; because some antitumor markers increase while tumor burden decreases, the immune microenvironment changes are multidirectional rather than a single scalar shift.
   - 类型：`ordinary`
   - 答案：`mixed`
   - 强度：`moderate`
   - 答案含义：多个 readouts 方向不同，不能用单一正/负方向概括。

## bio_006_uchl5_hnscc

Target paper: *In vivo CRISPR screening in head and neck cancer reveals Uchl5 as an immunotherapy target*
PMID: 41022734

1. **bio_006_v2_q01**
   - 问题：`in vivo CRISPR knockout screening` 对 `identification of Uchl5 as an immune-evasion gene` 的影响方向是什么？
   - Relation: `changes`
   - Context: A syngeneic head and neck squamous cell carcinoma mouse model was screened in vivo to find tumor-intrinsic genes whose loss changes immune sensitivity and response to immune checkpoint blockade.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

2. **bio_006_v2_q02**
   - 问题：`Uchl5 deficiency` 对 `CD8-positive T-cell infiltration` 的影响方向是什么？
   - Relation: `changes`
   - Context: Uchl5-deficient HNSCC tumors were evaluated in immunocompetent mice to test whether loss of this deubiquitinating enzyme increases antitumor T-cell entry into the tumor microenvironment.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

3. **bio_006_v2_q03**
   - 问题：`Uchl5 deficiency` 对 `anti-PD1 treatment response` 的影响方向是什么？
   - Relation: `changes`
   - Context: Orthotopic and syngeneic HNSCC mouse models were used to test whether tumors lacking Uchl5 become more sensitive to anti-PD1 immune checkpoint blockade.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_006_v2_q04**
   - 问题：`Uchl5 deficiency plus anti-PD1 treatment` 对 `tumor growth in immunocompetent mice` 的影响方向是什么？
   - Relation: `changes`
   - Context: Uchl5-deficient tumor cells were implanted into immunocompetent C57BL/6 mice and treated with anti-PD1; tumor growth was compared with Uchl5-intact controls to assess immune-dependent tumor control.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

5. **bio_006_v2_q05**
   - 问题：`Uchl5 deficiency` 对 `anti-PD1 response in NSG immunodeficient mice` 的影响方向是什么？
   - Relation: `changes`
   - Context: A context-shift comparison asks whether the benefit of Uchl5 loss persists in NSG mice lacking adaptive immunity; this tests whether the effect depends on an intact antitumor immune system.
   - 类型：`context_shift`
   - 答案：`null`
   - 强度：`unknown`
   - 答案含义：在这个 context 下，target paper 没有显示明显改变。

6. **bio_006_v2_q06**
   - 问题：`Uchl5 deficiency` 对 `survival after immune checkpoint blockade` 的影响方向是什么？
   - Relation: `changes`
   - Context: Mouse HNSCC models were followed after Uchl5 perturbation and checkpoint blockade to determine whether increased immune sensitivity translates into improved survival outcomes.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

## bio_007_fh15_colitis

Target paper: *Fh15 Reduces Colonic Inflammation and Leukocyte Infiltration in a Dextran Sulfate Sodium-Induced Ulcerative Colitis Mouse Model*
PMID: 40497975

1. **bio_007_v2_q01**
   - 问题：`Fh15 treatment` 对 `disease activity index in DSS-induced ulcerative colitis` 的影响方向是什么？
   - Relation: `changes`
   - Context: Male C57BL/6 mice received 4% DSS in drinking water to induce ulcerative colitis and were treated intraperitoneally with recombinant Fh15 on days 1, 3, and 5; daily DAI integrated body-weight loss, stool consistency, and bleeding severity.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

2. **bio_007_v2_q02**
   - 问题：`Fh15 treatment` 对 `colon-shortening severity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Colon length was measured after DSS exposure as an indirect marker of inflammation and tissue damage; Fh15-treated DSS mice were compared against DSS-only controls.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

3. **bio_007_v2_q03**
   - 问题：`Fh15 treatment` 对 `histopathological colitis score` 的影响方向是什么？
   - Relation: `changes`
   - Context: H&E-stained distal colon sections from DSS and DSS+Fh15 groups were scored for inflammatory and tissue-damage changes to assess whether treatment ameliorated microscopic disease severity.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

4. **bio_007_v2_q04**
   - 问题：`Fh15 treatment` 对 `TNF-alpha and IL-1beta expression in distal colon` 的影响方向是什么？
   - Relation: `changes`
   - Context: RT-PCR was used to measure pro-inflammatory cytokine expression in distal colon tissue from DSS-induced colitis mice treated with Fh15 versus DSS-only controls.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

5. **bio_007_v2_q05**
   - 问题：`Fh15 treatment` 对 `neutrophil and macrophage infiltration in colon tissue` 的影响方向是什么？
   - Relation: `changes`
   - Context: Immunohistochemistry quantified Ly6G-positive neutrophils and F4/80-positive macrophages in colonic samples from DSS-induced colitis mice with or without Fh15 treatment.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

6. **bio_007_v2_q06**
   - 问题：`Fh15 treatment` 对 `CD86 expression on spleen CD11b-positive CD11c-negative cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Flow cytometry of splenocytes from DSS and DSS+Fh15 mice measured CD86 expression within the CD11b-positive CD11c-negative cell population to test whether Fh15 reduces systemic myeloid activation markers.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

## bio_008_cryo_pd1_cervical

Target paper: *Cryoablation synergizes with anti-PD-1 immunotherapy induces an effective abscopal effect in murine model of cervical cancer*
PMID: 39489086

1. **bio_008_v2_q01**
   - 问题：`cryoablation combined with anti-PD-1 antibody` 对 `distant untreated tumor growth` 的影响方向是什么？
   - Relation: `changes`
   - Context: A murine U14 bilateral subcutaneous cervical cancer model was used: one tumor received local cryoablation while the contralateral tumor was left untreated to measure systemic abscopal tumor control under anti-PD-1 combination therapy.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

2. **bio_008_v2_q02**
   - 问题：`cryoablation combined with anti-PD-1 antibody` 对 `mouse survival` 的影响方向是什么？
   - Relation: `changes`
   - Context: Survival was followed in cervical-cancer-bearing mice treated with local cryoablation, anti-PD-1 antibody, their combination, or control treatment to determine whether systemic tumor control translated into survival benefit.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

3. **bio_008_v2_q03**
   - 问题：`cryoablation or cryoablation plus anti-PD-1 treatment` 对 `CD8-positive T-cell infiltration in distant tumors` 的影响方向是什么？
   - Relation: `changes`
   - Context: Distant non-ablated tumors were analyzed after treatment to test whether local cryoablation and checkpoint blockade increase cytotoxic T-cell infiltration at untreated tumor sites.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_008_v2_q04**
   - 问题：`cryoablation combined with anti-PD-1 antibody` 对 `M2-like tumor-associated macrophages and myeloid-derived suppressor cells` 的影响方向是什么？
   - Relation: `changes`
   - Context: Immune profiling of distant tumors tested whether the combination therapy reduces immunosuppressive myeloid populations while promoting a more antitumor immune microenvironment.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

5. **bio_008_v2_q05**
   - 问题：`anti-PD-1 antibody monotherapy without cryoablation` 对 `strong abscopal tumor control` 的影响方向是什么？
   - Relation: `changes`
   - Context: The bilateral cervical cancer model included anti-PD-1 treatment without local cryoablation; this context tests whether checkpoint blockade alone generated the strong systemic abscopal effect seen with the combination.
   - 类型：`context_shift`
   - 答案：`null`
   - 强度：`unknown`
   - 答案含义：在这个 context 下，target paper 没有显示明显改变。

6. **bio_008_v2_q06**
   - 问题：`cryoablation combined with anti-PD-1 antibody` 对 `overall distant-tumor immune microenvironment` 的影响方向是什么？
   - Relation: `changes`
   - Context: The target paper measured both effector immune features and suppressive cell populations in distant tumors; the combined therapy is expected to increase antitumor cells while decreasing suppressive myeloid populations.
   - 类型：`ordinary`
   - 答案：`mixed`
   - 强度：`moderate`
   - 答案含义：多个 readouts 方向不同，不能用单一正/负方向概括。

## bio_009_gastric_crispr

Target paper: *Gastric Organoid-Based Ectopic and Orthotopic In Vivo CRISPR Screening for Tumor Suppressors in Gastric Cancer*
PMID: 41288537

1. **bio_009_v2_q01**
   - 问题：`Pten inactivation` 对 `gastric tumor size` 的影响方向是什么？
   - Relation: `changes`
   - Context: Gastric organoid-based ectopic and orthotopic in vivo CRISPR screens perturbed candidate tumor suppressors; tumors with Pten inactivation were compared with other genotypes to assess growth-promoting effects.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`strong`
   - 答案含义：X 使该 outcome 增加、增强或改善。

2. **bio_009_v2_q02**
   - 问题：`Pten inactivation` 对 `neo-angiogenesis in large gastric tumors` 的影响方向是什么？
   - Relation: `changes`
   - Context: Large gastric tumors generated through organoid-based CRISPR perturbation were analyzed for vascular or angiogenic features to test whether Pten loss promotes a more angiogenic tumor phenotype.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

3. **bio_009_v2_q03**
   - 问题：`Pten inactivation` 对 `neutrophil recruitment and T-cell exclusion` 的影响方向是什么？
   - Relation: `changes`
   - Context: The tumor immune microenvironment in Pten-inactivated gastric tumors was profiled to assess whether loss of Pten is associated with neutrophil-rich and T-cell-excluded immune architecture.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

4. **bio_009_v2_q04**
   - 问题：`Smad4, Tgfbr1, or Acvr2a inactivation` 对 `intestinal metaplasia and compensatory hyperplasia-like phenotypes` 的影响方向是什么？
   - Relation: `changes`
   - Context: Specific TGF-beta pathway-related tumor suppressor perturbations were evaluated in gastric organoid-derived tumors to determine whether they produce gastric epithelial phenotypes resembling intestinal metaplasia or compensatory hyperplasia.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

5. **bio_009_v2_q05**
   - 问题：`Helicobacter pylori infection` 对 `tumor mutational landscape` 的影响方向是什么？
   - Relation: `changes`
   - Context: The CRISPR gastric tumor models were studied in the presence or absence of H. pylori to test whether the pathogen altered tumor genetics directly rather than mainly reshaping the tumor microenvironment.
   - 类型：`null_control`
   - 答案：`null`
   - 强度：`unknown`
   - 答案含义：在这个 context 下，target paper 没有显示明显改变。

6. **bio_009_v2_q06**
   - 问题：`Helicobacter pylori infection` 对 `tumor-promoting SiglecF-positive neutrophil recruitment` 的影响方向是什么？
   - Relation: `changes`
   - Context: The gastric tumor microenvironment was profiled after H. pylori exposure to test whether infection recruits a neutrophil population with tumor-promoting features rather than altering only tumor-cell genotype.
   - 类型：`ordinary`
   - 答案：`positive`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 增加、增强或改善。

## bio_010_if_colitis

Target paper: *Intermittent Fasting Reduces Intestinal Inflammation in Dextran Sulfate Sodium-Induced Colitis of Mice*
PMID: 39898122

1. **bio_010_v2_q01**
   - 问题：`intermittent fasting intervention` 对 `intestinal inflammation in DSS-induced colitis` 的影响方向是什么？
   - Relation: `changes`
   - Context: Mice underwent repeated DSS-induced colitis cycles, and intermittent fasting was applied during later cycles; intestinal inflammation was evaluated using disease signs, colon morphology, histology, and immune-cell readouts.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

2. **bio_010_v2_q02**
   - 问题：`intermittent fasting intervention` 对 `disease activity index or visible colitis symptoms` 的影响方向是什么？
   - Relation: `changes`
   - Context: During chronic DSS cycles, DAI components such as occult blood, stool changes, and body-weight loss were monitored to test whether intermittent fasting reduced clinical disease severity compared with DSS controls.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

3. **bio_010_v2_q03**
   - 问题：`intermittent fasting intervention` 对 `DSS-mediated colon-shortening severity` 的影响方向是什么？
   - Relation: `changes`
   - Context: Colon length was measured after repeated DSS exposure to test whether fasting mitigated the structural shortening associated with chronic colitis injury.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

4. **bio_010_v2_q04**
   - 问题：`intermittent fasting intervention` 对 `colonic histological injury score` 的影响方向是什么？
   - Relation: `changes`
   - Context: Colon sections were scored on a 0-4 histological scale covering mucosal inflammation, edema, and crypt injury after DSS with or without intermittent fasting intervention.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

5. **bio_010_v2_q05**
   - 问题：`intermittent fasting intervention` 对 `CD4-positive T-cell proportion in spleen and mesenteric lymph nodes` 的影响方向是什么？
   - Relation: `changes`
   - Context: Immune-cell populations in systemic and gut-draining lymphoid tissues were profiled after DSS colitis and fasting intervention to evaluate whether adaptive immune-cell proportions changed with reduced inflammation.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

6. **bio_010_v2_q06**
   - 问题：`intermittent fasting intervention` 对 `macrophage infiltration around the crypt base` 的影响方向是什么？
   - Relation: `changes`
   - Context: Colonic immune infiltration was assessed around crypt-base regions after DSS-induced injury to test whether fasting reduced macrophage accumulation associated with intestinal inflammation.
   - 类型：`ordinary`
   - 答案：`negative`
   - 强度：`moderate`
   - 答案含义：X 使该 outcome 降低、减弱或被抑制。

