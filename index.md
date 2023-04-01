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

{: .success }
**Welcome to DSC 10! 👋 Start by reading the [Syllabus](syllabus) and completing the action items in the [Getting Started](syllabus#-getting-started) section. See you on Monday!**

<!-- [Jump to the current week](#week-10){: .btn } -->

{% for module in site.modules %}
{{ module }}
{% endfor %}