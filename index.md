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
Check out [**this**](https://edstem.org/us/courses/38383/discussion/3014984) post on Ed to see clarifications to common misconceptions, and [**this**](https://edstem.org/us/courses/38383/discussion/3029800) post to find a partner for the Midterm Project!

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-4-probability-and-simulation){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}