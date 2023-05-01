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
**Look [here](https://edstem.org/us/courses/38383/discussion/3048533) for important information about this Friday's Midterm Exam. If at least 75% of the class completes the [Mid-Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSctWbIQTzYYGmTAx8pg-nWE1nGUFLyU0D4hHZ9-0rccG39imQ/viewform) by 12PM on Friday, then everyone will receive an extra 2% on the Midterm Exam!**

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-4-probability-and-simulation){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}