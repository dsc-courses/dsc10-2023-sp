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
Check out [**this post on Ed**](https://edstem.org/us/courses/38383/discussion/3014984) to see clarifications to common misconceptions, and come to the parter-finding mixer on Wednesday 4/26 from 1:30-2:15PM in the Center Hall courtyard!

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-3-visualization-and-more-dataframes){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}