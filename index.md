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
The [Diagrams](diagrams) page of the course website has been updated to include **all** diagrams that will be used for the remainder of the quarter – including diagrams on permutation testing and bootstrapping.

Below, you can open "static" versions of each lecture by clicking the ✏️ emojis and watch podcasts by clicking the 🎥 emojis.

[Jump to the current week](#week-6-hypothesis-testing-br-small-there-won-t-be-live-lecture-on-wednesday-or-friday-since-suraj-is-at-a-a-href-https-cfp-jupytercon-com-2023-talk-xabs9s-conference-a-notebooks-and-videos-for-those-lectures-have-already-been-posted-below-on-wednesday-from-1-1-50pm-in-center-109-tutors-will-take-up-common-misconceptions-from-the-midterm-exam-small){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}