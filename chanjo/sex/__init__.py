# -*- coding: utf-8 -*-
"""Component for guessing the sex from a BAM alignment.

The component reads coverage for subsections of each sex chromosome.
Based on the ratio between the average coverage across chromosomes it
makes a simple sex prediction.
"""
from .core import sex_from_bam
