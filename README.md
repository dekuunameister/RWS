# RWS
Things I wrote for the Radiation Weather Station (RWS), a University of Michigan lab funded by the US Department of Energy.  I was brought on to this all-undergraduate research team to develop software and perform data analysis.

EXPLANATION OF THE FILES:
rename_most_recent.py:
Solved a problem that had been going on for over a year in which one of our lab instruments (ORTEC sword) would overwrite existing files every time it rebooted.  The reason was that the then-current version of our data collection had the instrument name new files with a numerical system e.g. 00, 01, 100.  When it had to reboot, it would start over from 00, which meant the previous 00-suffixed file would be completely written over.  I solved this issue by having the script go into the directory with all the data files and rename them according to date and time before the next file could get pushed by the lab device.

calc_roi_area.py:
The ORTEC sword mentioned above collects quantities of numerous atmospheric radioactive isotopes.  Interesting portions of the resulting graph can be isolated by taking the area under "regions of interest", which appear as peaks in this polynomial line graph.  My script averages the left and right Riemann sums for peaks and returns that area.
