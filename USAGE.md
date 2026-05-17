# 菴ｿ縺・婿繧ｬ繧､繝・窶・GOOD STACK

---

## 蜑肴署譚｡莉ｶ・亥・蝗槭・縺ｿ・・
```powershell
# 莉ｮ諠ｳ迺ｰ蠅・ｒ譛牙柑蛹厄ｼ域ｯ主屓蠢・ｦ・ｼ・cd C:\Users\oueno\venv\good-stack
.venv\Scripts\activate
```

`.env` 縺ｫ莉･荳九・繧ｭ繝ｼ縺瑚ｨｭ螳壹＆繧後※縺・ｋ縺薙→・・
```
GOOGLE_API_KEY=AIza...        # Gemini API・郁ｨ倅ｺ狗函謌撰ｼ・LLM_MODEL=gemini-2.5-flash
PEXELS_API_KEY=...            # Pexels API・郁ｨ倅ｺ狗判蜒上・辟｡譁呻ｼ・```

- Gemini API繧ｭ繝ｼ蜿門ｾ怜・: https://aistudio.google.com/app/apikey
- Pexels API繧ｭ繝ｼ蜿門ｾ怜・: https://www.pexels.com/api/・育┌譁吶・逋ｻ骭ｲ縺ｮ縺ｿ・・
---

## 險倅ｺ九ｒ逕滓・縺吶ｋ

逕滓・縺輔ｌ縺溯ｨ倅ｺ九・ `site/content/articles/YYYYMMDDHH-slug.md` 縺ｮ蠖｢蠑上〒菫晏ｭ倥＆繧後∪縺吶・ 
Pexels API繧ｭ繝ｼ縺瑚ｨｭ螳壹＆繧後※縺・ｌ縺ｰ**繝偵・繝ｭ繝ｼ逕ｻ蜒・譫夲ｼ区悽譁・・逕ｻ蜒・譫・*縺瑚・蜍輔〒莉倥″縺ｾ縺吶・
### 繝代ち繝ｼ繝ｳ竭 繝｢繝・け逕滓・・・PI繧ｭ繝ｼ荳崎ｦ√・蜍穂ｽ懃｢ｺ隱咲畑・・
```powershell
# 繝ｬ繧ｸ繧ｹ繝医Μ縺九ｉ谺｡縺ｮ繝医ヴ繝・け繧定・蜍暮∈謚槭＠縺ｦ逕滓・
python scripts\local_generate.py --mock

# 繝医ヴ繝・け繧呈欠螳壹＠縺ｦ逕滓・
python scripts\local_generate.py --topic "Echo Dot 繧ｱ繝ｼ繧ｹ 縺翫☆縺吶ａ" --mock
```

- AI繧剃ｽｿ繧上★繝・Φ繝励Ξ繝ｼ繝域枚遶縺ｧ蜊ｳ譎ら函謌撰ｼ育判蜒上・莉倥°縺ｪ縺・ｼ・- 陦ｨ遉ｺ繝ｻ讒矩縺ｮ遒ｺ隱阪↓菴ｿ縺・
### 繝代ち繝ｼ繝ｳ竭｡ Gemini逕滓・・磯壼ｸｸ・・
```powershell
# 繝ｬ繧ｸ繧ｹ繝医Μ縺九ｉ谺｡縺ｮ繝医ヴ繝・け繧定・蜍暮∈謚・python scripts\local_generate.py

# 繝医ヴ繝・け繧呈欠螳・python scripts\local_generate.py --topic "繧ｹ繝槭・繝医・繝ｩ繧ｰ 縺翫☆縺吶ａ 遽髮ｻ"
```

- Gemini API縺瑚ｨ倅ｺ九ｒ蝓ｷ遲・￣exels縺九ｉ逕ｻ蜒上ｒ閾ｪ蜍募叙蠕・- 謇隕∵凾髢・ 30遘偵・蛻・
### 繝代ち繝ｼ繝ｳ竭｢ Google讀懃ｴ｢縺､縺咲函謌撰ｼ域怙鬮伜刀雉ｪ・・
```powershell
# 繝ｬ繧ｸ繧ｹ繝医Μ縺九ｉ谺｡縺ｮ繝医ヴ繝・け繧定・蜍暮∈謚・python scripts\local_generate.py --search

# 繝医ヴ繝・け繧呈欠螳・python scripts\local_generate.py --topic "繧ｹ繝槭・繝医・繝ｩ繧ｰ 縺翫☆縺吶ａ 遽髮ｻ" --search
```

- Google讀懃ｴ｢縺ｧ譛譁ｰ縺ｮ陬ｽ蜩∵ュ蝣ｱ繝ｻ萓｡譬ｼ繝ｻ繝ｬ繝薙Η繝ｼ繧貞叙蠕励＠縺ｦ縺九ｉ蝓ｷ遲・- Pexels縺九ｉ逕ｻ蜒上ｒ閾ｪ蜍募叙蠕暦ｼ医ヲ繝ｼ繝ｭ繝ｼ1譫夲ｼ区悽譁・譫夲ｼ・- 謇隕∵凾髢・ 1縲・蛻・- 豬√ｌ: `Google讀懃ｴ｢荳ｭ...` 竊・`險倅ｺ九ｒ逕滓・荳ｭ...` 竊・`Images fetched: 3 photos` 竊・螳御ｺ・
### 繝輔Λ繧ｰ縺ｮ縺ｾ縺ｨ繧・
| 繝輔Λ繧ｰ | 諢丞袖 |
|---|---|
| 縺ｪ縺・| Gemini縺ｧ騾壼ｸｸ逕滓・繝ｻ逕ｻ蜒丈ｻ倥″ |
| `--mock` | API縺ｪ縺励・繝・Φ繝励Ξ繝ｼ繝医〒蜊ｳ譎ら函謌撰ｼ育判蜒上↑縺暦ｼ・|
| `--search` | Google讀懃ｴ｢縺ｧ譛譁ｰ諠・ｱ繧貞叙蠕励＠縺ｦ縺九ｉ逕滓・繝ｻ逕ｻ蜒丈ｻ倥″ |
| `--topic "..."` | 繝医ヴ繝・け繧堤峩謗･謖・ｮ夲ｼ育怐逡･縺吶ｋ縺ｨ繝ｬ繧ｸ繧ｹ繝医Μ縺九ｉ閾ｪ蜍暮∈謚橸ｼ・|

---

## 繧ｵ繧､繝医ｒ繝ｭ繝ｼ繧ｫ繝ｫ縺ｧ遒ｺ隱阪☆繧・
```powershell
# 繧ｿ繝ｼ繝溘リ繝ｫ繧貞挨縺ｫ髢九＞縺ｦHugo髢狗匱繧ｵ繝ｼ繝舌・繧定ｵｷ蜍・cd site
hugo server --buildDrafts --buildFuture --navigateToChanged
```

繝悶Λ繧ｦ繧ｶ縺ｧ **http://localhost:1313/amazon-affiliate-site/** 繧帝幕縺上・
險倅ｺ九ｒ逕滓・縺吶ｋ縺溘・縺ｫ繝悶Λ繧ｦ繧ｶ縺・*閾ｪ蜍輔〒繝ｪ繝ｭ繝ｼ繝・*縺輔ｌ繧九・
---

## 險倅ｺ九ヵ繧｡繧､繝ｫ縺ｮ讒区・

逕滓・縺輔ｌ縺櫪arkdown繝輔ぃ繧､繝ｫ縺ｮ繝輔Ο繝ｳ繝医・繧ｿ繝ｼ萓具ｼ・
```yaml
---
title: Echo Show 15 縺翫☆縺吶ａ繧｢繧ｯ繧ｻ繧ｵ繝ｪ繝ｼ縺ｾ縺ｨ繧・slug: echo-show-15-accessories-guide
date: '2026-05-16T14:30:00'   # 逕滓・縺励◆譎ょ綾・育ｧ貞腰菴搾ｼ・description: ...
tags: [...]
categories: [...]
image: https://images.pexels.com/...  # 繝偵・繝ｭ繝ｼ逕ｻ蜒酋RL
draft: false
---
```

- 繝輔ぃ繧､繝ｫ蜷・ `2026051614-echo-show-15-accessories-guide.md`・亥ｹｴ譛域律譎・繧ｹ繝ｩ繝・げ・・- URL縺ｯ `slug:` 繝輔ぅ繝ｼ繝ｫ繝峨〒豎ｺ縺ｾ繧九・縺ｧ繝輔ぃ繧､繝ｫ蜷阪・譌･譎ゅ・URL縺ｫ蠖ｱ髻ｿ縺励↑縺・- 蜷梧律縺ｫ隍・焚險倅ｺ九ｒ逕滓・縺励※繧よ凾蛻ｻ縺ｧ鬆・分縺悟玄蛻･縺輔ｌ繧・
---

## 繝医ヴ繝・け繧堤ｮ｡逅・☆繧・
繝医ヴ繝・け縺ｯ `topic_registry.json`・郁・蜍慕函謌撰ｼ峨〒邂｡逅・＆繧後ｋ縲・
```powershell
# 谿九ｊ繝医ヴ繝・け謨ｰ繧堤｢ｺ隱・python -c "from generator.topic_registry import TopicRegistry; r=TopicRegistry(); print(f'谿九ｊ: {r.pending_count()}莉ｶ')"
```

### 繝医ヴ繝・け繧定｣懷・縺吶ｋ・医ヨ繝ｬ繝ｳ繝峨°繧芽・蜍募叙蠕暦ｼ・
```powershell
# Google Trends + Gemini grounding 縺ｮ荳｡譁ｹ縺九ｉ蜿門ｾ暦ｼ域耳螂ｨ・・python scripts\refresh_topics.py

# Gemini縺ｮ縺ｿ・・oogle Trends縺碁≦縺・・繧ｨ繝ｩ繝ｼ縺ｮ譎ゑｼ・python scripts\refresh_topics.py --source gemini

# 繧ｸ繝｣繝ｳ繝ｫ繧呈欠螳壹＠縺ｦ邨槭ｊ霎ｼ繧・・oogle Trends繝ｻGemini 荳｡譁ｹ縺ｫ驕ｩ逕ｨ・・python scripts\refresh_topics.py --seeds "繧ｭ繝｣繝ｳ繝・繧｢繧ｦ繝医ラ繧｢" "逋ｻ螻ｱ 繧ｬ繧ｸ繧ｧ繝・ヨ"

# 霑ｽ蜉縺帙★蜿門ｾ礼ｵ先棡縺縺醍｢ｺ隱阪☆繧・python scripts\refresh_topics.py --dry-run

# pending 縺・莉ｶ莉･荳九・譎ゅ□縺題｣懷・縺吶ｋ
python scripts\refresh_topics.py --min-pending 5

# 繧ｭ繝｣繝ｳ繝励・繧｢繧ｦ繝医ラ繧｢邉ｻ縺ｫ邨槭ｋ
python scripts/refresh_topics.py --seeds "繧ｭ繝｣繝ｳ繝・繧｢繧ｦ繝医ラ繧｢" "逋ｻ螻ｱ 繧ｬ繧ｸ繧ｧ繝・ヨ"

# 繧ｹ繝槭・繝ｻiPhone邉ｻ縺ｫ邨槭ｋ
python scripts/refresh_topics.py --seeds "iPhone 繧｢繧ｯ繧ｻ繧ｵ繝ｪ繝ｼ" "Android 繧ｹ繝槭・"

# 蟄｣遽繝・・繝槭〒邨槭ｋ・亥､丞ｮｶ髮ｻ縺ｪ縺ｩ・・python scripts/refresh_topics.py --seeds "螟・螳ｶ髮ｻ" "遽髮ｻ 繧ｰ繝・ぜ"

# 遒ｺ隱阪＠縺ｦ縺九ｉ霑ｽ蜉
python scripts/refresh_topics.py --seeds "繧ｭ繝｣繝ｳ繝・ --dry-run

# Gemini縺縺托ｼ・oogle Trends縺碁≦縺・凾・・python scripts/refresh_topics.py --source gemini --seeds "繧ｭ繝｣繝ｳ繝・
```

### 繝医ヴ繝・け繧堤峩謗･霑ｽ蜉縺吶ｋ

```powershell
# 莉ｻ諢上・繝医ヴ繝・け繧堤峩謗･霑ｽ蜉
python scripts\refresh_topics.py --add "iPhone 16 Pro 繧ｱ繝ｼ繧ｹ 縺翫☆縺吶ａ"

# 隍・焚縺ｾ縺ｨ繧√※霑ｽ蜉
python scripts\refresh_topics.py --add "iPad Air 繧ｹ繧ｿ繝ｳ繝・ "AirPods 繧ｱ繝ｼ繧ｹ 豈碑ｼ・

# 霑ｽ蜉蜑阪↓遒ｺ隱阪＠縺溘＞蝣ｴ蜷・python scripts\refresh_topics.py --add "譁ｰ縺励＞繝医ヴ繝・け" --dry-run
```

| 繝輔Λ繧ｰ | 諢丞袖 |
|---|---|
| 縺ｪ縺・| Google Trends + Gemini 荳｡譁ｹ縺九ｉ繝医ヴ繝・け繧貞叙蠕励＠縺ｦ霑ｽ蜉 |
| `--source gemini` | Gemini grounding縺ｮ縺ｿ |
| `--source google` | Google Trends縺ｮ縺ｿ |
| `--seeds "..."` | 謖・ｮ壹く繝ｼ繝ｯ繝ｼ繝峨・繧ｸ繝｣繝ｳ繝ｫ縺ｫ邨槭ｊ霎ｼ繧・井ｸ｡譁ｹ縺ｫ驕ｩ逕ｨ・・|
| `--add "..."` | 繝医ヴ繝・け繧堤峩謗･謖・ｮ壹＠縺ｦ霑ｽ蜉・医ヨ繝ｬ繝ｳ繝牙叙蠕励↑縺暦ｼ・|
| `--dry-run` | 霑ｽ蜉縺帙★邨先棡縺縺題｡ｨ遉ｺ |
| `--min-pending N` | pending 縺・N 莉ｶ莉･荳翫≠繧後・繧ｹ繧ｭ繝・・ |

---

## 繝・せ繝医ｒ螳溯｡後☆繧・
```powershell
python -m pytest tests/ -v
```

---

## 蛻ｩ逕ｨ蜿ｯ閭ｽ縺ｪGemini繝｢繝・Ν繧堤｢ｺ隱阪☆繧・
```powershell
python scripts\list_models.py
```

`.env` 縺ｮ `LLM_MODEL=` 縺ｫ繝｢繝・Ν蜷阪ｒ險ｭ螳壹☆繧具ｼ・models/` 繝励Ξ繝輔ぅ繝・け繧ｹ縺ｯ荳崎ｦ・ｼ峨・
---

## GitHub Actions縺ｧ閾ｪ蜍慕函謌舌☆繧具ｼ亥・髢句ｾ鯉ｼ・
### 險倅ｺ狗函謌撰ｼ・enerate Articles・・
GitHub縺ｮ繝ｪ繝昴ず繝医Μ繝壹・繧ｸ 竊・**Actions** 繧ｿ繝・竊・**Generate Articles** 竊・**Run workflow**

| 蜈･蜉帶ｬ・| 隱ｬ譏・|
|---|---|
| topic | 遨ｺ谺・↑繧芽・蜍暮∈謚槭∝・蜉帙☆繧九→謖・ｮ壹ヨ繝斐ャ繧ｯ縺ｧ逕滓・ |
| use_mock | `true` 縺ｫ縺吶ｋ縺ｨAPI繧ｭ繝ｼ荳崎ｦ√・繝｢繝・け逕滓・ |

繧ｹ繧ｱ繧ｸ繝･繝ｼ繝ｫ閾ｪ蜍募ｮ溯｡・ **譛医・豌ｴ繝ｻ驥・蜊亥燕9譎・ST**

### 繝医ヴ繝・け陬懷・・・efresh Topics・・
GitHub縺ｮ繝ｪ繝昴ず繝医Μ繝壹・繧ｸ 竊・**Actions** 繧ｿ繝・竊・**Refresh Topics** 竊・**Run workflow**

| 蜈･蜉帶ｬ・| 隱ｬ譏・|
|---|---|
| source | `both`・医ョ繝輔か繝ｫ繝茨ｼ・ `gemini` / `google` |
| min_pending | pending 縺後％縺ｮ莉ｶ謨ｰ莉･荳翫↑繧芽｣懷・繧偵せ繧ｭ繝・・・医ョ繝輔か繝ｫ繝・ 5・・|

繧ｹ繧ｱ繧ｸ繝･繝ｼ繝ｫ閾ｪ蜍募ｮ溯｡・ **豈朱ｱ譌･譖・蜊亥燕9譎・ST**

GitHub Secrets 縺ｫ `GOOGLE_API_KEY` 縺ｨ `PEXELS_API_KEY` 縺ｮ荳｡譁ｹ繧堤匳骭ｲ縺励※縺翫￥縺薙→縲・
---

## 繧医￥縺ゅｋ繧ｨ繝ｩ繝ｼ縺ｨ蟇ｾ蜃ｦ

| 繧ｨ繝ｩ繝ｼ | 蜴溷屏 | 蟇ｾ蜃ｦ |
|---|---|---|
| `GOOGLE_API_KEY` 縺瑚ｦ九▽縺九ｉ縺ｪ縺・| `.env` 縺梧悴菴懈・ | `.env.example` 繧偵さ繝斐・縺励※ `.env` 繧剃ｽ懈・ |
| `429 RESOURCE_EXHAUSTED` limit:0 | API繧ｭ繝ｼ縺ｮ辟｡譁呎棧縺梧怏蜉ｹ縺ｧ縺ｪ縺・| 蛻･縺ｮAPI繧ｭ繝ｼ繧堤匱陦後☆繧九°隱ｲ驥題ｨｭ螳壹ｒ遒ｺ隱・|
| `404 NOT_FOUND` 繝｢繝・Ν縺瑚ｦ九▽縺九ｉ縺ｪ縺・| 繝｢繝・Ν蜷阪′蜿､縺・| `python scripts\list_models.py` 縺ｧ遒ｺ隱阪＠縺ｦ `.env` 繧呈峩譁ｰ |
| Hugo縺瑚ｪ崎ｭ倥＆繧後↑縺・| PATH縺梧悴譖ｴ譁ｰ | VSCode繧貞・襍ｷ蜍輔＠縺ｦ縺九ｉ隧ｦ縺・|
| 逕ｻ蜒上′陦ｨ遉ｺ縺輔ｌ縺ｪ縺・| `PEXELS_API_KEY` 譛ｪ險ｭ螳・| `.env` 縺ｫ `PEXELS_API_KEY` 繧定ｿｽ蜉 |
| 險倅ｺ九′陦ｨ遉ｺ縺輔ｌ縺ｪ縺・| 譌･譎ゅ′譛ｪ譚･縺ｫ縺ｪ縺｣縺ｦ縺・ｋ | 險倅ｺ九・ `date:` 繧堤樟蝨ｨ譎ょ綾繧医ｊ驕主悉縺ｫ菫ｮ豁｣ |
| CSS 縺悟渚譏縺輔ｌ縺ｪ縺・ｼ・hrome・・| 繝悶Λ繧ｦ繧ｶ繧ｭ繝｣繝・す繝･縺悟商縺・| F12竊呈峩譁ｰ繝懊ち繝ｳ蜿ｳ繧ｯ繝ｪ繝・け竊偵後く繝｣繝・す繝･縺ｮ豸亥悉縺ｨ繝上・繝牙・隱ｭ縺ｿ霎ｼ縺ｿ縲・|
| CSS 縺悟渚譏縺輔ｌ縺ｪ縺・| Hugo繧ｵ繝ｼ繝舌・繧貞・襍ｷ蜍輔＠縺ｦ縺・↑縺・| Ctrl+C 縺ｧ豁｢繧√※蜀崎ｵｷ蜍・|
| CSS縺悟ｮ悟・縺ｫ隱ｭ縺ｿ霎ｼ縺ｾ繧後↑縺・ｼ・04・・| CSS繝ｪ繝ｳ繧ｯ縺梧悽逡ｪURL繧呈欠縺励※縺・ｋ | `head.html` 縺ｧ `absURL` 繧剃ｽｿ繧上★ `relURL` 繧剃ｽｿ縺・ｼ井ｿｮ豁｣貂医∩・・|
| 險倅ｺ九・繝ｼ繧ｸ縺ｫhero逕ｻ蜒上・繝代Φ縺上★繝ｻ繧ｿ繧ｰ縺悟・縺ｪ縺・| `_default/page.html` 縺・`single.html` 繧医ｊ蜆ｪ蜈医＆繧後※縺・ｋ | `page.html` 繧貞炎髯､縺吶ｋ・井ｿｮ豁｣貂医∩・・|
| 險倅ｺ九′陦ｨ遉ｺ縺輔ｌ縺ｪ縺・ｼ亥､憺俣逕滓・・・| 逕滓・譎ょ綾縺梧悴譚･謇ｱ縺・↓縺ｪ繧・| `--buildFuture` 繝輔Λ繧ｰ莉倥″縺ｧ繧ｵ繝ｼ繝舌・襍ｷ蜍包ｼ医ョ繝輔か繝ｫ繝域ｸ医∩・・|

