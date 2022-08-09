# Masked Copy Number Segment #
## Description ##

The Masked Copy Number Segment files are a version of the [Copy Number Segment](LINK) files with segments removed if they are likely to contain germline variation.   

## Overview ##

The GDC generates Masked Copy Number Segment files by filtering Copy Number Segment files. If a segment contains an array probe that is known to correspond to germline variants, that segment is removed. The list of array probes associated with germline variation can be downloaded at the [GDC Reference File](https://gdc.cancer.gov/about-data/data-harmonization-and-generation/gdc-reference-files) page.

### Data Formats ###

See the [Copy Number Segment](LINK) page for format details.

## References ##
1. [GDC CNV Documentation](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/CNV_Pipeline/)

## External Links ##
* N/A

Categories: Data Type
