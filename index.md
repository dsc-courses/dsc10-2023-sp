---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

{: .note }
<b>There won't be live lecture on Wednesday or Friday, since Suraj is at a <a href="https://cfp.jupytercon.com/2023/talk/XABS9S/">conference</a>. Notebooks and videos for those lectures have already been posted [below](#week-5-midterm-exam). On Wednesday from 1-1:50PM in Center 109, tutors will take up common misconceptions from the Midterm Exam.</b>

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-5-midterm-exam){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}