# Biology Pilot 问题与答案

这个文件使用 `target_papers.md` 中之前选出的 10 篇 biology / biomedical target papers，整理出一版可读的中文问题与答案。

注意：这里沿用当前 `biology_pilot_instances.jsonl` 的标签体系。`positive` 表示“这个关系陈述被 target paper 支持”，不一定表示第二个变量数值升高。例如：

```text
BTLA agonist treatment reduces airway inflammation -> positive
```

意思是论文支持“BTLA agonist 会减少 airway inflammation”。正式 v2 数据集建议把 relation 改成更中性的 `affects / changes / regulates`，这样 `positive / negative` 就可以直接表示数值方向。

当前统计：

- Target papers: 10
- Questions: 60
- Ordinary questions: 38
- Null controls: 3
- Decoy-relation controls: 11
- Context-shift controls: 8
- Gold labels: 38 positive, 5 null, 17 unsupported

这些问题和答案是 pilot draft。正式使用前，需要逐篇核验 full text、figures、tables 和 supplement。

## 1. bio_001_inulin_colitis

Target paper: *Inulin aggravates colitis through gut microbiota modulation and MyD88/IL-18 signaling*

1. 问题：在 DSS-induced colitis mouse model 中，inulin supplementation 是否会加重 intestinal inflammation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持这个关系。inulin 在 DSS 结肠炎模型中加重肠道炎症。
   - 强度：strong

2. 问题：在 steady-state mice without DSS colitis challenge 中，inulin supplementation 是否会诱导 intestinal inflammation？
   - 类型：null_control
   - 答案：null
   - 含义：论文语境下没有明显支持 inulin 在无 DSS 挑战的稳态小鼠中单独诱导肠炎。
   - 强度：unknown

3. 问题：在 DSS-induced colitis mouse model with MyD88/IL-18 signaling 中，microbiota-derived flagellin signaling 是否介导 inulin-associated colitis aggravation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 microbiota / flagellin / MyD88 / IL-18 相关机制参与 inulin 加重结肠炎。
   - 强度：moderate

4. 问题：在 DSS-induced colitis mouse model 中，inulin supplementation 是否改善 colon barrier integrity？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。当前 target paper 的主要发现不支持“inulin 改善屏障完整性”这个结论。
   - 强度：unknown

5. 问题：在 DSS-induced colitis mouse model 中，inulin supplementation 是否减少 IL-18 signaling？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。该说法与论文的 MyD88/IL-18 机制方向不匹配。
   - 强度：unknown

6. 问题：在 microbiota-depleted DSS-induced colitis mice 中，inulin supplementation 是否会加重 intestinal inflammation？
   - 类型：context_shift
   - 答案：null
   - 含义：换成 microbiota-depleted context 后，inulin 加重炎症的效应预计消失或不明显。
   - 强度：unknown

## 2. bio_002_btla_asthma

Target paper: *BTLA agonist attenuates Th17-driven inflammation in a mouse model of steroid-resistant asthma*

1. 问题：在 Th17-driven steroid-resistant asthma mouse model 中，BTLA agonist treatment 是否减少 airway inflammation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 BTLA agonist 减轻气道炎症。
   - 强度：moderate

2. 问题：在 BXD75 house-dust-mite asthma model 中，BTLA agonist treatment 是否减少 airway hyperreactivity？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 BTLA agonist 降低气道高反应性。
   - 强度：moderate

3. 问题：在 ex vivo Th17 cell treatment 中，BTLA agonist treatment 是否降低 IL-17 levels？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 BTLA agonist 抑制 Th17 / IL-17 相关炎症信号。
   - 强度：moderate

4. 问题：在 Th17 cells treated ex vivo 中，BTLA agonist treatment 是否抑制 NF-kB signaling？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 BTLA agonist 抑制 NF-kB signaling。
   - 强度：moderate

5. 问题：在 allergic asthma model not characterized as Th17-driven steroid-resistant asthma 中，BTLA agonist treatment 是否减少 eosinophilic inflammation？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是语境转移题。target paper 关注 Th17-driven steroid-resistant asthma，不支持把结论直接外推到 eosinophilic allergic asthma。
   - 强度：unknown

6. 问题：在 Th17-driven steroid-resistant asthma mouse model 中，BTLA agonist treatment 是否增加 IL-4 production？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 主要不是证明 BTLA agonist 增加 IL-4。
   - 强度：unknown

## 3. bio_003_intestinimonas_metabolic

Target paper: *Gut bacterium Intestinimonas butyriciproducens improves host metabolic health*

1. 问题：在 diet-induced obesity mouse model 中，Intestinimonas butyriciproducens administration 是否改善 host metabolic health？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该菌干预改善代谢健康。
   - 强度：moderate

2. 问题：在 diet-induced obesity mouse model 中，Intestinimonas butyriciproducens administration 是否减少 inguinal white adipose tissue inflammation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该菌降低白色脂肪组织炎症。
   - 强度：moderate

3. 问题：在 inguinal white adipose tissue in diet-induced obese mice 中，Intestinimonas butyriciproducens administration 是否促进 adipose browning pathways？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该菌促进脂肪 browning 相关通路。
   - 强度：moderate

4. 问题：在 diet-induced obesity mouse model 中，Intestinimonas butyriciproducens administration 是否促进 insulin signaling pathways？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该菌改善或促进 insulin signaling。
   - 强度：moderate

5. 问题：在 mouse colorectal cancer model 中，Intestinimonas butyriciproducens administration 是否减少 colonic tumor burden？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 的主要语境是代谢健康和 obesity，不是 colorectal cancer tumor burden。
   - 强度：unknown

6. 问题：在 lean chow-fed mice without diet-induced obesity 中，Intestinimonas butyriciproducens administration 是否改善 host metabolic health？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是语境转移题。target paper 的效果主要在 diet-induced obesity 语境下，不应直接外推到 lean chow-fed mice。
   - 强度：unknown

## 4. bio_004_crispr_colon

Target paper: *A Novel CRISPR/Cas9-mediated Mouse Model of Colon Carcinogenesis*

1. 问题：在 mouse colon epithelium targeting Apc, Pten, Trp53, and Smad4 中，inducible multiplexed CRISPR/Cas9 mutagenesis 是否生成 sporadic colorectal tumors？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该 CRISPR/Cas9 设计能建立散发性结直肠肿瘤模型。
   - 强度：strong

2. 问题：在 CRISPR/Cas9-mediated mouse colon carcinogenesis model 中，gut-specific PLAGL2 overexpression 是否增加 colon tumor growth？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 PLAGL2 overexpression 促进肿瘤生长。
   - 强度：moderate

3. 问题：在 inducible multiplexed CRISPR/Cas9 mouse model 中，somatic inactivation of Apc, Pten, Trp53, and Smad4 是否模拟 multi-step colorectal cancer pathogenesis？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持该模型可模拟多步骤结直肠癌发生。
   - 强度：moderate

4. 问题：在 CRISPR/Cas9-mediated mouse colon carcinogenesis model 中，gut-specific PLAGL2 overexpression 是否降低 colon tumor growth？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是反向干扰关系。target paper 支持的是 PLAGL2 促进而不是降低肿瘤生长。
   - 强度：unknown

5. 问题：在 mouse colon carcinogenesis model 中，inducible multiplexed CRISPR/Cas9 mutagenesis 是否测试 anti-PD1 treatment response？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。该 target paper 不是 anti-PD1 response benchmark。
   - 强度：unknown

6. 问题：在 sporadic colorectal cancer modeling 中，CRISPR/Cas9-mediated colon carcinogenesis model 是否需要 chemical DSS-induced colitis？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是语境转移题。该模型不是 DSS colitis 依赖的结肠炎癌变模型。
   - 强度：unknown

## 5. bio_005_mwa_ici

Target paper: *Microwave ablation combined with immune checkpoint inhibitor enhanced antitumor immune activation and memory*

1. 问题：在 rechallenged tumor mouse model 中，microwave ablation combined with immune checkpoint inhibitor 是否增强 antitumor immune activation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持联合治疗增强抗肿瘤免疫激活。
   - 强度：moderate

2. 问题：在 rechallenged tumor mouse model 中，microwave ablation monotherapy 是否抑制 rechallenged tumor growth？
   - 类型：null_control
   - 答案：null
   - 含义：单独 microwave ablation 在该 rechallenge 语境中没有明显达到联合治疗那样的抑制效果。
   - 强度：unknown

3. 问题：在 rechallenged tumor mouse model 中，microwave ablation monotherapy 是否上调 PD-L1 expression on tumor cells？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 ablation 后 PD-L1 表达上调，为联合 checkpoint inhibitor 提供机制基础。
   - 强度：moderate

4. 问题：在 rechallenged tumor mouse model 中，microwave ablation combined with immune checkpoint inhibitor 是否增强 antitumor immune memory？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持联合治疗增强抗肿瘤免疫记忆。
   - 强度：moderate

5. 问题：在 rechallenged tumor mouse model 中，microwave ablation combined with immune checkpoint inhibitor 是否减少 gut inflammation？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 关注 tumor immunity，不支持 gut inflammation 结论。
   - 强度：unknown

6. 问题：在 rechallenged tumor mouse model after microwave ablation study design 中，immune checkpoint inhibitor monotherapy 是否诱导 durable antitumor immune memory？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是语境/治疗方案转移题。target paper 的主结论是联合治疗，不是 ICI 单药。
   - 强度：unknown

## 6. bio_006_uchl5_hnscc

Target paper: *In vivo CRISPR screening in head and neck cancer reveals Uchl5 as an immunotherapy target*

1. 问题：在 head and neck squamous cell carcinoma mouse model 中，in vivo CRISPR screening 是否识别 Uchl5 as an immune evasion gene？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Uchl5 是免疫逃逸相关基因。
   - 强度：moderate

2. 问题：在 orthotopic 4MOSC1 HNSCC mouse model 中，Uchl5 deficiency 是否增强 anti-PD1 treatment response？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Uchl5 缺失提高 anti-PD1 治疗响应。
   - 强度：moderate

3. 问题：在 immunocompetent C57BL/6 mice with anti-PD1 treatment 中，Uchl5-deficient tumor cells 是否减少 tumor growth？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持在免疫完整小鼠和 anti-PD1 语境下，Uchl5-deficient tumors 生长降低。
   - 强度：moderate

4. 问题：在 NSG immunodeficient mice lacking adaptive immunity 中，Uchl5 deficiency 是否增强 anti-PD1 response？
   - 类型：context_shift
   - 答案：null
   - 含义：换成缺乏适应性免疫的 NSG 小鼠后，Uchl5 缺失对 anti-PD1 response 的增强预计不明显。
   - 强度：unknown

5. 问题：在 head and neck cancer mouse model 中，Uchl5 overexpression 是否改善 anti-PD1 treatment response？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是反向/干扰关系。target paper 支持 Uchl5 deficiency 有利，而不是 overexpression 改善 response。
   - 强度：unknown

6. 问题：在 HNSCC tumors treated with anti-PD1 中，Uchl5 deficiency 是否增加 antitumor immune sensitivity？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Uchl5 deficiency 增加肿瘤对抗肿瘤免疫的敏感性。
   - 强度：moderate

## 7. bio_007_fh15_colitis

Target paper: *Fh15 reduces colonic inflammation and leukocyte infiltration in a DSS-induced ulcerative colitis mouse model*

1. 问题：在 DSS-induced ulcerative colitis male mice 中，Fh15 treatment 是否减少 disease activity index？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Fh15 降低疾病活动指数。
   - 强度：strong

2. 问题：在 DSS-induced ulcerative colitis male mice 中，Fh15 treatment 是否防止 colon shortening？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Fh15 缓解或防止 DSS 造成的结肠缩短。
   - 强度：moderate

3. 问题：在 distal colon tissue in DSS-induced colitis mice 中，Fh15 treatment 是否下调 TNF-alpha and IL-1beta？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Fh15 降低炎症细胞因子。
   - 强度：moderate

4. 问题：在 colon tissue in DSS-induced ulcerative colitis mice 中，Fh15 treatment 是否减少 neutrophil and macrophage infiltration？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Fh15 减少中性粒细胞和巨噬细胞浸润。
   - 强度：strong

5. 问题：在 DSS-induced ulcerative colitis mice 中，Fh15 treatment 是否改善 sleep quality？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 不研究 sleep quality。
   - 强度：unknown

6. 问题：在 female mice with DSS-induced ulcerative colitis 中，Fh15 treatment 是否减少 colonic inflammation？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是语境转移题。target paper 当前问题限定 male mice，不应直接外推到 female mice。
   - 强度：unknown

## 8. bio_008_cryo_pd1_cervical

Target paper: *Cryoablation synergizes with anti-PD-1 immunotherapy induces an effective abscopal effect in murine model of cervical cancer*

1. 问题：在 U14 murine bilateral subcutaneous cervical cancer model 中，cryoablation combined with anti-PD-1 antibody 是否抑制 distant tumor growth？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 cryoablation + anti-PD-1 产生远端肿瘤控制效果。
   - 强度：strong

2. 问题：在 murine cervical cancer model 中，cryoablation combined with anti-PD-1 antibody 是否改善 mouse survival？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持联合治疗改善生存。
   - 强度：moderate

3. 问题：在 distant tumors in murine cervical cancer model 中，cryoablation 是否增加 CD8-positive T cell infiltration？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 cryoablation 增加远端肿瘤 CD8+ T cell infiltration。
   - 强度：moderate

4. 问题：在 distant tumors in murine cervical cancer model 中，cryoablation combined with anti-PD-1 antibody 是否减少 M2-like tumor-associated macrophages and myeloid-derived suppressor cells？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持联合治疗降低免疫抑制性细胞群。
   - 强度：moderate

5. 问题：在 murine bilateral cervical cancer model without cryoablation 中，anti-PD-1 antibody monotherapy 是否诱导 strong abscopal tumor control？
   - 类型：context_shift
   - 答案：unsupported
   - 含义：这是治疗方案转移题。target paper 的 strong abscopal effect 依赖联合 cryoablation。
   - 强度：unknown

6. 问题：在 murine cervical cancer model 中，cryoablation combined with anti-PD-1 antibody 是否减少 intestinal inflammation？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 关注 cervical cancer tumor immunity，不是 intestinal inflammation。
   - 强度：unknown

## 9. bio_009_gastric_crispr

Target paper: *Gastric organoid-based ectopic and orthotopic in vivo CRISPR screening for tumor suppressors in gastric cancer*

1. 问题：在 gastric organoid-based in vivo CRISPR mouse model 中，Pten inactivation 是否增加 tumor size？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Pten inactivation 促进胃肿瘤增大。
   - 强度：strong

2. 问题：在 large gastric tumors in CRISPR mouse model 中，Pten inactivation 是否增加 neo-angiogenesis？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Pten inactivation 与新生血管生成增加相关。
   - 强度：moderate

3. 问题：在 gastric tumors in CRISPR mouse model 中，Pten inactivation 是否增加 neutrophil recruitment and T-cell exclusion？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 Pten inactivation 促进中性粒细胞招募和 T-cell exclusion。
   - 强度：moderate

4. 问题：在 gastric organoid-based in vivo CRISPR mouse model 中，Smad4, Tgfbr1, or Acvr2a inactivation 是否产生 intestinal metaplasia and compensatory hyperplasia-like phenotypes？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持这些基因失活产生类似肠化生和代偿性增生的表型。
   - 强度：moderate

5. 问题：在 gastric organoid-based CRISPR mouse tumors 中，Helicobacter pylori infection 是否影响 tumor mutational landscape？
   - 类型：null_control
   - 答案：null
   - 含义：论文语境下 H. pylori 不一定改变 tumor mutational landscape，主要作用更偏向 microenvironment。
   - 强度：unknown

6. 问题：在 gastric tumor microenvironment in CRISPR mouse model 中，Helicobacter pylori infection 是否招募 tumor-promoting SiglecF-positive neutrophils？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 H. pylori 改变肿瘤微环境并招募促肿瘤的 SiglecF+ neutrophils。
   - 强度：moderate

## 10. bio_010_if_colitis

Target paper: *Intermittent fasting reduces intestinal inflammation in DSS-induced colitis of mice*

1. 问题：在 DSS-induced colitis mouse model 中，intermittent fasting 是否减少 intestinal inflammation？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 intermittent fasting 减轻肠道炎症。
   - 强度：moderate

2. 问题：在 DSS-induced colitis mouse model 中，intermittent fasting 是否逆转 DSS-mediated colon shortening？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 intermittent fasting 缓解 DSS 导致的结肠缩短。
   - 强度：moderate

3. 问题：在 DSS-induced colitis mouse model 中，intermittent fasting 是否降低 colonic histological score？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 intermittent fasting 改善组织学炎症评分。
   - 强度：moderate

4. 问题：在 spleen and mesenteric lymph nodes in DSS-induced colitis mice 中，intermittent fasting 是否减少 CD4-positive T cell proportion？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 intermittent fasting 改变免疫细胞组成并降低 CD4+ T cell proportion。
   - 强度：moderate

5. 问题：在 DSS-induced colitis mouse study 中，intermittent fasting 是否改善 anti-PD1 tumor immunotherapy response？
   - 类型：decoy_relation
   - 答案：unsupported
   - 含义：这是干扰关系。target paper 是 colitis / fasting 研究，不是 anti-PD1 tumor immunotherapy。
   - 强度：unknown

6. 问题：在 DSS-induced colitis mouse colon 中，intermittent fasting 是否减少 macrophage infiltration around the crypt base？
   - 类型：ordinary
   - 答案：positive
   - 含义：论文支持 intermittent fasting 减少 crypt base 周围 macrophage infiltration。
   - 强度：moderate

## Quantitative 问题候选

下面这些是适合加入 correlation / effect-size 的问题，但目前不能直接填 `gold_numeric_value`，因为必须先从 target paper 的 full text、figure、table 或 supplement 中核验真实数值。

1. `bio_003_intestinimonas_metabolic`
   - 问题：在人群 cohort 中，Intestinimonas abundance 与 metabolic-health markers 的相关系数是多少？
   - 方向答案：预计 positive
   - 数值答案：待全文核验
   - 建议 metric：`correlation_r`

2. `bio_003_intestinimonas_metabolic`
   - 问题：在 diet-induced obese mice 中，Intestinimonas administration 对 adipose inflammation 的 effect size 是多少？
   - 方向答案：预计 negative effect on inflammation / 当前 relation statement 可记为 positive support for reduction
   - 数值答案：待全文核验
   - 建议 metric：`percent_change` 或 `mean_difference`

3. `bio_007_fh15_colitis`
   - 问题：Fh15 treatment 对 disease activity index 的平均差异或百分比变化是多少？
   - 方向答案：预计降低 DAI
   - 数值答案：待全文核验
   - 建议 metric：`mean_difference` 或 `percent_change`

4. `bio_007_fh15_colitis`
   - 问题：Fh15 treatment 对 colon length 的 effect size 是多少？
   - 方向答案：预计缓解 colon shortening
   - 数值答案：待全文核验
   - 建议 metric：`mean_difference`

5. `bio_010_if_colitis`
   - 问题：intermittent fasting 对 colonic histological score 的数值降低幅度是多少？
   - 方向答案：预计降低 histological score
   - 数值答案：待全文核验
   - 建议 metric：`mean_difference` 或 `percent_change`

6. `bio_010_if_colitis`
   - 问题：intermittent fasting 对 CD4-positive T-cell proportion 的 percentage-point change 是多少？
   - 方向答案：预计降低 CD4+ T-cell proportion
   - 数值答案：待全文核验
   - 建议 metric：`percentage_point_change`

7. `bio_008_cryo_pd1_cervical`
   - 问题：cryoablation plus anti-PD-1 对 distant tumor volume 的降低幅度是多少？
   - 方向答案：预计降低 tumor volume
   - 数值答案：待全文核验
   - 建议 metric：`tumor_volume_ratio` 或 `percent_change`

8. `bio_008_cryo_pd1_cervical`
   - 问题：cryoablation plus anti-PD-1 的 survival benefit 是多少？
   - 方向答案：预计提高 survival
   - 数值答案：待全文核验
   - 建议 metric：`survival_days`、`hazard_ratio` 或 `median_survival_ratio`

9. `bio_009_gastric_crispr`
   - 问题：Pten inactivation 对 gastric tumor size 的 fold change 或 mean difference 是多少？
   - 方向答案：预计增加 tumor size
   - 数值答案：待全文核验
   - 建议 metric：`fold_change`、`mean_difference` 或 `tumor_volume_ratio`

10. `bio_006_uchl5_hnscc`
    - 问题：Uchl5 deficiency 对 anti-PD1 treatment response 的数值改善幅度是多少？
    - 方向答案：预计改善 anti-PD1 response
    - 数值答案：待全文核验
    - 建议 metric：`tumor_volume_ratio`、`percent_change` 或 `response_rate_difference`
