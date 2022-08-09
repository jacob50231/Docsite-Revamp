# Appendix A: Available Fields

The GDC API's [search and retrieval endpoints](Search_and_Retrieval.md) provide access to fields that correspond to properties defined in the [GDC Data Dictionary](../../Data_Dictionary/viewer.md). This appendix contains a list of fields available at each endpoint, and a list of field groups accessible via the [expand parameter](Search_and_Retrieval.md#expand).

## Field Listing by Endpoint

### Project Fields

| Field Name |
| --- | -------- |
| dbgap_accession_number |
| disease_type |
| name |  
| primary_site |
| project_id |
| released |
| state |
| program.dbgap_accession_number |
| program.name |  
| program.program_id |
| summary.case_count |
| summary.file_count |
| summary.file_size |
| summary.data_categories.case_count |
| summary.data_categories.data_category |
| summary.data_categories.file_count |
| summary.experimental_strategies.case_count |  
| summary.experimental_strategies.experimental_strategy |
| summary.experimental_strategies.file_count |



### Case Fields


| Field Name |
| --- | -------- |
| aliquot_ids |
| analyte_ids |
| case_id |
| created_datetime |  
| days_to_index |  
| portion_ids |
| sample_ids |
| slide_ids |
| state |
| submitter_aliquot_ids |
| submitter_analyte_ids |
| submitter_id |
| submitter_portion_ids |
| submitter_sample_ids |
| submitter_slide_ids |
| updated_datetime |  
| annotations.annotation_id |
| annotations.case_id |
| annotations.case_submitter_id |
| annotations.category |
| annotations.classification |
| annotations.created_datetime |
| annotations.creator |
| annotations.entity_id |
| annotations.entity_submitter_id |
| annotations.entity_type |
| annotations.legacy_created_datetime |
| annotations.legacy_updated_datetime |
| annotations.notes |
| annotations.state |
| annotations.status |
| annotations.submitter_id |
| annotations.updated_datetime |
| demographic.created_datetime |
| demographic.demographic_id |
| demographic.ethnicity |
| demographic.gender |
| demographic.race |
| demographic.state |
| demographic.submitter_id |
| demographic.updated_datetime |
| demographic.year_of_birth |
| demographic.year_of_death |
| diagnoses.age_at_diagnosis |
| diagnoses.classification_of_tumor |
| diagnoses.created_datetime |
| diagnoses.days_to_birth |
| diagnoses.days_to_death |
| diagnoses.days_to_last_follow_up |
| diagnoses.days_to_last_known_disease_status |
| diagnoses.days_to_recurrence |
| diagnoses.diagnosis_id |
| diagnoses.last_known_disease_status |
| diagnoses.morphology |
| diagnoses.primary_diagnosis |
| diagnoses.prior_malignancy |
| diagnoses.progression_or_recurrence |
| diagnoses.site_of_resection_or_biopsy |
| diagnoses.state |
| diagnoses.submitter_id |
| diagnoses.tissue_or_organ_of_origin |
| diagnoses.tumor_grade |
| diagnoses.tumor_stage |
| diagnoses.updated_datetime |
| diagnoses.vital_status |
| diagnoses.treatments.created_datetime |
| diagnoses.treatments.days_to_treatment |
| diagnoses.treatments.state |
| diagnoses.treatments.submitter_id |
| diagnoses.treatments.therapeutic_agents |
| diagnoses.treatments.treatment_id |
| diagnoses.treatments.treatment_intent_type |
| diagnoses.treatments.treatment_or_therapy |
| diagnoses.treatments.updated_datetime |
| exposures.alcohol_history |
| exposures.alcohol_intensity |
| exposures.bmi |
| exposures.cigarettes_per_day |
| exposures.created_datetime |
| exposures.exposure_id |
| exposures.height |
| exposures.state |
| exposures.submitter_id |
| exposures.updated_datetime |
| exposures.weight |
| exposures.years_smoked |
| family_histories.created_datetime |
| family_histories.family_history_id |  
| family_histories.relationship_age_at_diagnosis |
| family_histories.relationship_gender |
| family_histories.relationship_primary_diagnosis |
| family_histories.relationship_type |
| family_histories.relative_with_cancer_history |
| family_histories.state |
| family_histories.submitter_id |
| family_histories.updated_datetime |
| files.access |
| files.acl |
| files.created_datetime |
| files.data_category |
| files.data_format |
| files.data_type |
| files.error_type |
| files.experimental_strategy |
| files.file_id |
| files.file_name |
| files.file_size |
| files.file_state |
| files.md5sum |
| files.origin |
| files.platform |
| files.revision |
| files.state |
| files.state_comment |
| files.submitter_id |
| files.tags |
| files.type |
| files.updated_datetime |
| files.analysis.analysis_id |
| files.analysis.analysis_type |
| files.analysis.created_datetime |
| files.analysis.state |
| files.analysis.submitter_id |
| files.analysis.updated_datetime |
| files.analysis.workflow_end_datetime |
| files.analysis.workflow_link |
| files.analysis.workflow_start_datetime |
| files.analysis.workflow_type |
| files.analysis.workflow_version |
| files.analysis.input_files.access |
| files.analysis.input_files.created_datetime |
| files.analysis.input_files.data_category |
| files.analysis.input_files.data_format |
| files.analysis.input_files.data_type |
| files.analysis.input_files.error_type |
| files.analysis.input_files.experimental_strategy |
| files.analysis.input_files.file_id |
| files.analysis.input_files.file_name |
| files.analysis.input_files.file_size |
| files.analysis.input_files.file_state |
| files.analysis.input_files.md5sum |
| files.analysis.input_files.platform |
| files.analysis.input_files.revision |
| files.analysis.input_files.state |
| files.analysis.input_files.state_comment |
| files.analysis.input_files.submitter_id |
| files.analysis.input_files.updated_datetime |
| files.analysis.metadata.read_groups.adapter_name |
| files.analysis.metadata.read_groups.adapter_sequence |
| files.analysis.metadata.read_groups.base_caller_name |
| files.analysis.metadata.read_groups.base_caller_version |
| files.analysis.metadata.read_groups.created_datetime |
| files.analysis.metadata.read_groups.experiment_name |
| files.analysis.metadata.read_groups.flow_cell_barcode |
| files.analysis.metadata.read_groups.includes_spike_ins |
| files.analysis.metadata.read_groups.instrument_model |
| files.analysis.metadata.read_groups.is_paired_end |
| files.analysis.metadata.read_groups.library_name |
| files.analysis.metadata.read_groups.library_preparation_kit_catalog_number |
| files.analysis.metadata.read_groups.library_preparation_kit_name |
| files.analysis.metadata.read_groups.library_preparation_kit_vendor |
| files.analysis.metadata.read_groups.library_preparation_kit_version |
| files.analysis.metadata.read_groups.library_selection |
| files.analysis.metadata.read_groups.library_strand |
| files.analysis.metadata.read_groups.library_strategy |
| files.analysis.metadata.read_groups.platform |
| files.analysis.metadata.read_groups.read_group_id |
| files.analysis.metadata.read_groups.read_group_name |
| files.analysis.metadata.read_groups.read_length |
| files.analysis.metadata.read_groups.RIN |
| files.analysis.metadata.read_groups.sequencing_center |
| files.analysis.metadata.read_groups.sequencing_date |
| files.analysis.metadata.read_groups.size_selection_range |
| files.analysis.metadata.read_groups.spike_ins_concentration |
| files.analysis.metadata.read_groups.spike_ins_fasta |
| files.analysis.metadata.read_groups.state |
| files.analysis.metadata.read_groups.submitter_id |
| files.analysis.metadata.read_groups.target_capture_kit_catalog_number |
| files.analysis.metadata.read_groups.target_capture_kit_name |
| files.analysis.metadata.read_groups.target_capture_kit_target_region |
| files.analysis.metadata.read_groups.target_capture_kit_vendor |
| files.analysis.metadata.read_groups.target_capture_kit_version |
| files.analysis.metadata.read_groups.to_trim_adapter_sequence |
| files.analysis.metadata.read_groups.updated_datetime |
| files.analysis.metadata.read_groups.read_group_qcs.adapter_content |
| files.analysis.metadata.read_groups.read_group_qcs.basic_statistics |
| files.analysis.metadata.read_groups.read_group_qcs.created_datetime |
| files.analysis.metadata.read_groups.read_group_qcs.encoding |
| files.analysis.metadata.read_groups.read_group_qcs.fastq_name |
| files.analysis.metadata.read_groups.read_group_qcs.kmer_content |
| files.analysis.metadata.read_groups.read_group_qcs.overrepresented_sequences |
| files.analysis.metadata.read_groups.read_group_qcs.per_base_n_content |
| files.analysis.metadata.read_groups.read_group_qcs.per_base_sequence_content |
| files.analysis.metadata.read_groups.read_group_qcs.per_base_sequence_quality |
| files.analysis.metadata.read_groups.read_group_qcs.per_sequence_gc_content |
| files.analysis.metadata.read_groups.read_group_qcs.per_sequence_quality_score |
| files.analysis.metadata.read_groups.read_group_qcs.per_tile_sequence_quality |
| files.analysis.metadata.read_groups.read_group_qcs.percent_gc_content |
| files.analysis.metadata.read_groups.read_group_qcs.read_group_qc_id |
| files.analysis.metadata.read_groups.read_group_qcs.sequence_duplication_levels |
| files.analysis.metadata.read_groups.read_group_qcs.sequence_length_distribution |
| files.analysis.metadata.read_groups.read_group_qcs.state |
| files.analysis.metadata.read_groups.read_group_qcs.submitter_id |
| files.analysis.metadata.read_groups.read_group_qcs.total_sequences |
| files.analysis.metadata.read_groups.read_group_qcs.updated_datetime |
| files.analysis.metadata.read_groups.read_group_qcs.workflow_end_datetime |
| files.analysis.metadata.read_groups.read_group_qcs.workflow_link |
| files.analysis.metadata.read_groups.read_group_qcs.workflow_start_datetime |
| files.analysis.metadata.read_groups.read_group_qcs.workflow_type |
| files.analysis.metadata.read_groups.read_group_qcs.workflow_version |
| files.archive.archive_id |
| files.archive.created_datetime |
| files.archive.data_category |
| files.archive.data_format |
| files.archive.data_type |
| files.archive.error_type |
| files.archive.file_name |
| files.archive.file_size |
| files.archive.file_state |
| files.archive.md5sum |
| files.archive.revision |
| files.archive.state |
| files.archive.state_comment |
| files.archive.submitter_id |
| files.archive.updated_datetime |
| files.cases.aliquot_ids |
| files.cases.analyte_ids |
| files.cases.case_id |
| files.cases.created_datetime |
| files.cases.days_to_index |
| files.cases.portion_ids |
| files.cases.sample_ids |
| files.cases.slide_ids |
| files.cases.state |
| files.cases.submitter_aliquot_ids |
| files.cases.submitter_analyte_ids |
| files.cases.submitter_id |
| files.cases.submitter_portion_ids |
| files.cases.submitter_sample_ids |
| files.cases.submitter_slide_ids |
| files.cases.updated_datetime |
| files.cases.annotations.annotation_id |
| files.cases.annotations.case_id |
| files.cases.annotations.case_submitter_id |
| files.cases.annotations.category |
| files.cases.annotations.classification |
| files.cases.annotations.created_datetime |
| files.cases.annotations.creator |
| files.cases.annotations.entity_id |
| files.cases.annotations.entity_submitter_id |
| files.cases.annotations.entity_type |
| files.cases.annotations.legacy_created_datetime |
| files.cases.annotations.legacy_updated_datetime |
| files.cases.annotations.notes |
| files.cases.annotations.state |
| files.cases.annotations.status |
| files.cases.annotations.submitter_id |
| files.cases.annotations.updated_datetime |
| files.cases.demographic.created_datetime |
| files.cases.demographic.demographic_id |
| files.cases.demographic.ethnicity |
| files.cases.demographic.gender |
| files.cases.demographic.race |
| files.cases.demographic.state |
| files.cases.demographic.submitter_id |
| files.cases.demographic.updated_datetime |
| files.cases.demographic.year_of_birth |
| files.cases.demographic.year_of_death |
| files.cases.diagnoses.age_at_diagnosis |
| files.cases.diagnoses.classification_of_tumor |
| files.cases.diagnoses.created_datetime |
| files.cases.diagnoses.days_to_birth |
| files.cases.diagnoses.days_to_death |
| files.cases.diagnoses.days_to_last_follow_up |
| files.cases.diagnoses.days_to_last_known_disease_status |
| files.cases.diagnoses.days_to_recurrence |
| files.cases.diagnoses.diagnosis_id |
| files.cases.diagnoses.last_known_disease_status |
| files.cases.diagnoses.morphology |
| files.cases.diagnoses.primary_diagnosis |
| files.cases.diagnoses.prior_malignancy |
| files.cases.diagnoses.progression_or_recurrence |
| files.cases.diagnoses.site_of_resection_or_biopsy |
| files.cases.diagnoses.state |
| files.cases.diagnoses.submitter_id |
| files.cases.diagnoses.tissue_or_organ_of_origin |
| files.cases.diagnoses.tumor_grade |
| files.cases.diagnoses.tumor_stage |
| files.cases.diagnoses.updated_datetime |
| files.cases.diagnoses.vital_status |
| files.cases.diagnoses.treatments.created_datetime |
| files.cases.diagnoses.treatments.days_to_treatment |
| files.cases.diagnoses.treatments.state |
| files.cases.diagnoses.treatments.submitter_id |
| files.cases.diagnoses.treatments.therapeutic_agents |
| files.cases.diagnoses.treatments.treatment_id |
| files.cases.diagnoses.treatments.treatment_intent_type |
| files.cases.diagnoses.treatments.treatment_or_therapy |
| files.cases.diagnoses.treatments.updated_datetime |
| files.cases.exposures.alcohol_history |
| files.cases.exposures.alcohol_intensity |
| files.cases.exposures.bmi |
| files.cases.exposures.cigarettes_per_day |
| files.cases.exposures.created_datetime |
| files.cases.exposures.exposure_id |
| files.cases.exposures.height |
| files.cases.exposures.state |
| files.cases.exposures.submitter_id |
| files.cases.exposures.updated_datetime |
| files.cases.exposures.weight |
| files.cases.exposures.years_smoked |
| files.cases.family_histories.created_datetime |
| files.cases.family_histories.family_history_id |
| files.cases.family_histories.relationship_age_at_diagnosis |
| files.cases.family_histories.relationship_gender |
| files.cases.family_histories.relationship_primary_diagnosis |
| files.cases.family_histories.relationship_type |
| files.cases.family_histories.relative_with_cancer_history |
| files.cases.family_histories.state |
| files.cases.family_histories.submitter_id |
| files.cases.family_histories.updated_datetime |
| files.cases.files.created_datetime |
| files.cases.files.error_type |
| files.cases.files.file_id |
| files.cases.files.file_name |
| files.cases.files.file_size |
| files.cases.files.file_state |
| files.cases.files.md5sum |
| files.cases.files.state |
| files.cases.files.state_comment |
| files.cases.files.submitter_id |
| files.cases.files.updated_datetime |
| files.cases.project.dbgap_accession_number |
| files.cases.project.disease_type |
| files.cases.project.name |
| files.cases.project.primary_site |
| files.cases.project.project_id |
| files.cases.project.released |
| files.cases.project.state |
| files.cases.project.program.dbgap_accession_number |
| files.cases.project.program.name |
| files.cases.project.program.program_id |
| files.cases.samples.composition |
| files.cases.samples.created_datetime |
| files.cases.samples.current_weight |
| files.cases.samples.days_to_collection |
| files.cases.samples.days_to_sample_procurement |
| files.cases.samples.freezing_method |
| files.cases.samples.initial_weight |
| files.cases.samples.intermediate_dimension |
| files.cases.samples.is_ffpe |
| files.cases.samples.longest_dimension |
| files.cases.samples.oct_embedded |
| files.cases.samples.pathology_report_uuid |
| files.cases.samples.preservation_method |
| files.cases.samples.sample_id |
| files.cases.samples.sample_type |
| files.cases.samples.sample_type_id |
| files.cases.samples.shortest_dimension |
| files.cases.samples.state |
| files.cases.samples.submitter_id |
| files.cases.samples.time_between_clamping_and_freezing |
| files.cases.samples.time_between_excision_and_freezing |
| files.cases.samples.tissue_type |
| files.cases.samples.tumor_code |
| files.cases.samples.tumor_code_id |
| files.cases.samples.tumor_descriptor |
| files.cases.samples.updated_datetime |
| files.cases.samples.annotations.annotation_id |
| files.cases.samples.annotations.case_id |
| files.cases.samples.annotations.case_submitter_id |
| files.cases.samples.annotations.category |
| files.cases.samples.annotations.classification |
| files.cases.samples.annotations.created_datetime |
| files.cases.samples.annotations.creator |
| files.cases.samples.annotations.entity_id |
| files.cases.samples.annotations.entity_submitter_id |
| files.cases.samples.annotations.entity_type |
| files.cases.samples.annotations.legacy_created_datetime |
| files.cases.samples.annotations.legacy_updated_datetime |
| files.cases.samples.annotations.notes |
| files.cases.samples.annotations.state |
| files.cases.samples.annotations.status |
| files.cases.samples.annotations.submitter_id |
| files.cases.samples.annotations.updated_datetime |
| files.cases.samples.portions.created_datetime |
| files.cases.samples.portions.creation_datetime |
| files.cases.samples.portions.is_ffpe |
| files.cases.samples.portions.portion_id |
| files.cases.samples.portions.portion_number |
| files.cases.samples.portions.state |  
| files.cases.samples.portions.submitter_id |  
| files.cases.samples.portions.updated_datetime |
| files.cases.samples.portions.weight |
| files.cases.samples.portions.analytes.a260_a280_ratio |
| files.cases.samples.portions.analytes.amount |
| files.cases.samples.portions.analytes.analyte_id |
| files.cases.samples.portions.analytes.analyte_type |
| files.cases.samples.portions.analytes.analyte_type_id |
| files.cases.samples.portions.analytes.concentration |
| files.cases.samples.portions.analytes.created_datetime |
| files.cases.samples.portions.analytes.spectrophotometer_method |
| files.cases.samples.portions.analytes.state |
| files.cases.samples.portions.analytes.submitter_id |
| files.cases.samples.portions.analytes.updated_datetime |
| files.cases.samples.portions.analytes.well_number |
| files.cases.samples.portions.analytes.aliquots.aliquot_id |
| files.cases.samples.portions.analytes.aliquots.amount |
| files.cases.samples.portions.analytes.aliquots.analyte_type |
| files.cases.samples.portions.analytes.aliquots.analyte_type_id |
| files.cases.samples.portions.analytes.aliquots.concentration |
| files.cases.samples.portions.analytes.aliquots.created_datetime |
| files.cases.samples.portions.analytes.aliquots.source_center |
| files.cases.samples.portions.analytes.aliquots.state |
| files.cases.samples.portions.analytes.aliquots.submitter_id |
| files.cases.samples.portions.analytes.aliquots.updated_datetime |
| files.cases.samples.portions.analytes.aliquots.annotations.annotation_id |
| files.cases.samples.portions.analytes.aliquots.annotations.case_id |
| files.cases.samples.portions.analytes.aliquots.annotations.case_submitter_id |
| files.cases.samples.portions.analytes.aliquots.annotations.category |
| files.cases.samples.portions.analytes.aliquots.annotations.classification |
| files.cases.samples.portions.analytes.aliquots.annotations.created_datetime |
| files.cases.samples.portions.analytes.aliquots.annotations.creator |
| files.cases.samples.portions.analytes.aliquots.annotations.entity_id |
| files.cases.samples.portions.analytes.aliquots.annotations.entity_submitter_id |
| files.cases.samples.portions.analytes.aliquots.annotations.entity_type |
| files.cases.samples.portions.analytes.aliquots.annotations.legacy_created_datetime |
| files.cases.samples.portions.analytes.aliquots.annotations.legacy_updated_datetime |
| files.cases.samples.portions.analytes.aliquots.annotations.notes |
| files.cases.samples.portions.analytes.aliquots.annotations.state |
| files.cases.samples.portions.analytes.aliquots.annotations.status |
| files.cases.samples.portions.analytes.aliquots.annotations.submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.analytes.aliquots.annotations.updated_datetime |
| files.cases.samples.portions.analytes.aliquots.center.center_id |
| files.cases.samples.portions.analytes.aliquots.center.center_type |
| files.cases.samples.portions.analytes.aliquots.center.code |  Numeric code for the center
| files.cases.samples.portions.analytes.aliquots.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| files.cases.samples.portions.analytes.aliquots.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| files.cases.samples.portions.analytes.aliquots.center.short_name |  Shortened name of the center (e.g. BI)
| files.cases.samples.portions.analytes.annotations.annotation_id |
| files.cases.samples.portions.analytes.annotations.case_id |
| files.cases.samples.portions.analytes.annotations.case_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.analytes.annotations.category |  Top level characterization of the annotation
| files.cases.samples.portions.analytes.annotations.classification |  Top level classification of the annotation
| files.cases.samples.portions.analytes.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.analytes.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| files.cases.samples.portions.analytes.annotations.entity_id |
| files.cases.samples.portions.analytes.annotations.entity_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.analytes.annotations.entity_type |
| files.cases.samples.portions.analytes.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.analytes.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.analytes.annotations.notes |
| files.cases.samples.portions.analytes.annotations.state |
| files.cases.samples.portions.analytes.annotations.status |
| files.cases.samples.portions.analytes.annotations.submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.analytes.annotations.updated_datetime |
| files.cases.samples.portions.annotations.annotation_id |
| files.cases.samples.portions.annotations.case_id |
| files.cases.samples.portions.annotations.case_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.annotations.category |  Top level characterization of the annotation
| files.cases.samples.portions.annotations.classification |  Top level classification of the annotation
| files.cases.samples.portions.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| files.cases.samples.portions.annotations.entity_id |
| files.cases.samples.portions.annotations.entity_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.annotations.entity_type |
| files.cases.samples.portions.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.annotations.notes |
| files.cases.samples.portions.annotations.state |
| files.cases.samples.portions.annotations.status |
| files.cases.samples.portions.annotations.submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.annotations.updated_datetime |
| files.cases.samples.portions.center.center_id |
| files.cases.samples.portions.center.center_type |
| files.cases.samples.portions.center.code |  Numeric code for the center
| files.cases.samples.portions.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| files.cases.samples.portions.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| files.cases.samples.portions.center.short_name |  Shortened name of the center (e.g. BI)
| files.cases.samples.portions.slides.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.slides.number_proliferating_cells |  Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s)
| files.cases.samples.portions.slides.percent_eosinophil_infiltration |  Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s).
| files.cases.samples.portions.slides.percent_granulocyte_infiltration |
| files.cases.samples.portions.slides.percent_inflam_infiltration |  Numeric value to represent local response to cellular injury, marked by capillary dilatation, edema and leukocyte infiltration; clinically, inflammation is manifest by reddness, heat, pain, swelling and loss of function, with the need to heal damaged tissue
| files.cases.samples.portions.slides.percent_lymphocyte_infiltration |
| files.cases.samples.portions.slides.percent_monocyte_infiltration |
| files.cases.samples.portions.slides.percent_necrosis |
| files.cases.samples.portions.slides.percent_neutrophil_infiltration |
| files.cases.samples.portions.slides.percent_normal_cells |
| files.cases.samples.portions.slides.percent_stromal_cells |
| files.cases.samples.portions.slides.percent_tumor_cells |
| files.cases.samples.portions.slides.percent_tumor_nuclei |
| files.cases.samples.portions.slides.section_location |
| files.cases.samples.portions.slides.slide_id |
| files.cases.samples.portions.slides.state |  The current state of the object
| files.cases.samples.portions.slides.submitter_id |  The legacy barcode used before prior to the use UUIDs, varies by project
| files.cases.samples.portions.slides.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]\
| files.cases.samples.portions.slides.annotations.annotation_id |
| files.cases.samples.portions.slides.annotations.case_id |
| files.cases.samples.portions.slides.annotations.case_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.slides.annotations.category |  Top level characterization of the annotation
| files.cases.samples.portions.slides.annotations.classification |  Top level classification of the annotation
| files.cases.samples.portions.slides.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.slides.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| files.cases.samples.portions.slides.annotations.entity_id |
| files.cases.samples.portions.slides.annotations.entity_submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.slides.annotations.entity_type |
| files.cases.samples.portions.slides.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.slides.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.samples.portions.slides.annotations.notes |  Open entry for any further description or characterization of the data
| files.cases.samples.portions.slides.annotations.state |  The current state of the object
| files.cases.samples.portions.slides.annotations.status |  Status of the annotation
| files.cases.samples.portions.slides.annotations.submitter_id | Submitter supplied identifier information
| files.cases.samples.portions.slides.annotations.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| files.cases.summary.file_count |
| files.cases.summary.file_size |
| files.cases.summary.data_categories.data_category |
| files.cases.summary.data_categories.file_count |
| files.cases.summary.experimental_strategies.experimental_strategy |
| files.cases.summary.experimental_strategies.file_count |
| files.cases.tissue_source_site.bcr_id |
| files.cases.tissue_source_site.code |
| files.cases.tissue_source_site.name |
| files.cases.tissue_source_site.project |
| files.cases.tissue_source_site.tissue_source_site_id |
| files.center.center_id |
| files.center.center_type |
| files.center.code |  Numeric code for the center
| files.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| files.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| files.center.short_name |  Shortened name of the center (e.g. BI)
| files.downstream_analyses.analysis_id |
| files.downstream_analyses.analysis_type |
| files.downstream_analyses.created_datetime |
| files.downstream_analyses.state |
| files.downstream_analyses.submitter_id | Submitter supplied identifier information
| files.downstream_analyses.updated_datetime |
| files.downstream_analyses.workflow_end_datetime |
| files.downstream_analyses.workflow_link |
| files.downstream_analyses.workflow_start_datetime |
| files.downstream_analyses.workflow_type |
| files.downstream_analyses.workflow_version |
| files.downstream_analyses.output_files.access |
| files.downstream_analyses.output_files.created_datetime |
| files.downstream_analyses.output_files.data_category |
| files.downstream_analyses.output_files.data_format |
| files.downstream_analyses.output_files.data_type |
| files.downstream_analyses.output_files.error_type |
| files.downstream_analyses.output_files.experimental_strategy |
| files.downstream_analyses.output_files.file_id |
| files.downstream_analyses.output_files.file_name |
| files.downstream_analyses.output_files.file_size |
| files.downstream_analyses.output_files.file_state |
| files.downstream_analyses.output_files.md5sum |
| files.downstream_analyses.output_files.platform |
| files.downstream_analyses.output_files.revision |
| files.downstream_analyses.output_files.state |
| files.downstream_analyses.output_files.state_comment |
| files.downstream_analyses.output_files.submitter_id | Submitter supplied identifier information
| files.downstream_analyses.output_files.updated_datetime |
| files.index_files.access |
| files.index_files.created_datetime |
| files.index_files.data_category |
| files.index_files.data_format |
| files.index_files.data_type |
| files.index_files.error_type |
| files.index_files.experimental_strategy |
| files.index_files.file_id |
| files.index_files.file_name |
| files.index_files.file_size |
| files.index_files.file_state |
| files.index_files.md5sum |
| files.index_files.platform |
| files.index_files.revision |
| files.index_files.state |
| files.index_files.state_comment |
| files.index_files.submitter_id | Submitter supplied identifier information
| files.index_files.updated_datetime |
| files.metadata_files.access |
| files.metadata_files.created_datetime |
| files.metadata_files.data_category |
| files.metadata_files.data_format |
| files.metadata_files.data_type |
| files.metadata_files.error_type |
| files.metadata_files.file_id |
| files.metadata_files.file_name |
| files.metadata_files.file_size |
| files.metadata_files.file_state |
| files.metadata_files.md5sum |
| files.metadata_files.state |
| files.metadata_files.state_comment |
| files.metadata_files.submitter_id | Submitter supplied identifier information
| files.metadata_files.type |
| files.metadata_files.updated_datetime |
| project.dbgap_accession_number |  The dbgap accession number provided for the program
| project.disease_type |
| project.name |
| project.primary_site |
| project.project_id |
| project.released |
| project.state |
| project.program.dbgap_accession_number |
| project.program.name |
| project.program.program_id |
| samples.composition |
| samples.created_datetime |
| samples.current_weight |
| samples.days_to_collection |
| samples.days_to_sample_procurement |
| samples.freezing_method |
| samples.initial_weight |
| samples.intermediate_dimension |
| samples.is_ffpe |
| samples.longest_dimension |
| samples.oct_embedded |
| samples.pathology_report_uuid |
| samples.preservation_method |
| samples.sample_id |
| samples.sample_type |
| samples.sample_type_id |
| samples.shortest_dimension |
| samples.state |
| samples.submitter_id | Submitter supplied identifier information
| samples.time_between_clamping_and_freezing |
| samples.time_between_excision_and_freezing |
| samples.tissue_type |
| samples.tumor_code |
| samples.tumor_code_id |
| samples.tumor_descriptor |
| samples.updated_datetime |
| samples.annotations.annotation_id |
| samples.annotations.case_id |
| samples.annotations.case_submitter_id | Submitter supplied identifier information
| samples.annotations.category |  Top level characterization of the annotation
| samples.annotations.classification |  Top level classification of the annotation
| samples.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| samples.annotations.entity_id |
| samples.annotations.entity_submitter_id | Submitter supplied identifier information
| samples.annotations.entity_type |
| samples.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.annotations.notes |
| samples.annotations.state |
| samples.annotations.status |
| samples.annotations.submitter_id | Submitter supplied identifier information
| samples.annotations.updated_datetime |
| samples.portions.created_datetime |
| samples.portions.creation_datetime |
| samples.portions.is_ffpe |
| samples.portions.portion_id |
| samples.portions.portion_number |  Numeric value that represents the sequential number assigned to a portion of the sample.
| samples.portions.state |
| samples.portions.submitter_id | Submitter supplied identifier information
| samples.portions.updated_datetime |
| samples.portions.weight |
| samples.portions.analytes.a260_a280_ratio |
| samples.portions.analytes.amount |
| samples.portions.analytes.analyte_id |
| samples.portions.analytes.analyte_type |
| samples.portions.analytes.analyte_type_id |
| samples.portions.analytes.concentration |
| samples.portions.analytes.created_datetime |
| samples.portions.analytes.spectrophotometer_method |
| samples.portions.analytes.state |
| samples.portions.analytes.submitter_id | Submitter supplied identifier information
| samples.portions.analytes.updated_datetime |
| samples.portions.analytes.well_number |
| samples.portions.analytes.aliquots.aliquot_id |
| samples.portions.analytes.aliquots.amount |
| samples.portions.analytes.aliquots.analyte_type |
| samples.portions.analytes.aliquots.analyte_type_id |
| samples.portions.analytes.aliquots.concentration |
| samples.portions.analytes.aliquots.created_datetime |
| samples.portions.analytes.aliquots.source_center |
| samples.portions.analytes.aliquots.state |
| samples.portions.analytes.aliquots.submitter_id | Submitter supplied identifier information
| samples.portions.analytes.aliquots.updated_datetime |
| samples.portions.analytes.aliquots.annotations.annotation_id |
| samples.portions.analytes.aliquots.annotations.case_id |
| samples.portions.analytes.aliquots.annotations.case_submitter_id | Submitter supplied identifier information
| samples.portions.analytes.aliquots.annotations.category |  Top level characterization of the annotation
| samples.portions.analytes.aliquots.annotations.classification |  Top level classification of the annotation
| samples.portions.analytes.aliquots.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.aliquots.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| samples.portions.analytes.aliquots.annotations.entity_id |
| samples.portions.analytes.aliquots.annotations.entity_submitter_id | Submitter supplied identifier information
| samples.portions.analytes.aliquots.annotations.entity_type |
| samples.portions.analytes.aliquots.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.aliquots.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.aliquots.annotations.notes |
| samples.portions.analytes.aliquots.annotations.state |
| samples.portions.analytes.aliquots.annotations.status |
| samples.portions.analytes.aliquots.annotations.submitter_id | Submitter supplied identifier information
| samples.portions.analytes.aliquots.annotations.updated_datetime |
| samples.portions.analytes.aliquots.center.center_id |
| samples.portions.analytes.aliquots.center.center_type |
| samples.portions.analytes.aliquots.center.code |  Numeric code for the center
| samples.portions.analytes.aliquots.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| samples.portions.analytes.aliquots.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| samples.portions.analytes.aliquots.center.short_name |  Shortened name of the center (e.g. BI)
| samples.portions.analytes.annotations.annotation_id |
| samples.portions.analytes.annotations.case_id |
| samples.portions.analytes.annotations.case_submitter_id | Submitter supplied identifier information
| samples.portions.analytes.annotations.category |  Top level characterization of the annotation
| samples.portions.analytes.annotations.classification |  Top level classification of the annotation
| samples.portions.analytes.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| samples.portions.analytes.annotations.entity_id |
| samples.portions.analytes.annotations.entity_submitter_id | Submitter supplied identifier information
| samples.portions.analytes.annotations.entity_type |
| samples.portions.analytes.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.analytes.annotations.notes |
| samples.portions.analytes.annotations.state |
| samples.portions.analytes.annotations.status |
| samples.portions.analytes.annotations.submitter_id | Submitter supplied identifier information
| samples.portions.analytes.annotations.updated_datetime |
| samples.portions.annotations.annotation_id |
| samples.portions.annotations.case_id |
| samples.portions.annotations.case_submitter_id | Submitter supplied identifier information
| samples.portions.annotations.category |  Top level characterization of the annotation
| samples.portions.annotations.classification |  Top level classification of the annotation
| samples.portions.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| samples.portions.annotations.entity_id |
| samples.portions.annotations.entity_submitter_id | Submitter supplied identifier information
| samples.portions.annotations.entity_type |
| samples.portions.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.annotations.notes |
| samples.portions.annotations.state |
| samples.portions.annotations.status |
| samples.portions.annotations.submitter_id | Submitter supplied identifier information
| samples.portions.annotations.updated_datetime |
| samples.portions.center.center_id |
| samples.portions.center.center_type |
| samples.portions.center.code |  Numeric code for the center
| samples.portions.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| samples.portions.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| samples.portions.center.short_name |  Shortened name of the center (e.g. BI)
| samples.portions.slides.created_datetime |
| samples.portions.slides.number_proliferating_cells |  Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s)
| samples.portions.slides.percent_eosinophil_infiltration |
| samples.portions.slides.percent_granulocyte_infiltration |
| samples.portions.slides.percent_inflam_infiltration |
| samples.portions.slides.percent_lymphocyte_infiltration |
| samples.portions.slides.percent_monocyte_infiltration |
| samples.portions.slides.percent_necrosis |
| samples.portions.slides.percent_neutrophil_infiltration |
| samples.portions.slides.percent_normal_cells |
| samples.portions.slides.percent_stromal_cells |
| samples.portions.slides.percent_tumor_cells |
| samples.portions.slides.percent_tumor_nuclei |
| samples.portions.slides.section_location |
| samples.portions.slides.slide_id |
| samples.portions.slides.state |
| samples.portions.slides.submitter_id | Submitter supplied identifier information
| samples.portions.slides.updated_datetime |
| samples.portions.slides.annotations.annotation_id |
| samples.portions.slides.annotations.case_id |
| samples.portions.slides.annotations.case_submitter_id | Submitter supplied identifier information
| samples.portions.slides.annotations.category |  Top level characterization of the annotation
| samples.portions.slides.annotations.classification |  Top level classification of the annotation
| samples.portions.slides.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.slides.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| samples.portions.slides.annotations.entity_id |
| samples.portions.slides.annotations.entity_submitter_id | Submitter supplied identifier information
| samples.portions.slides.annotations.entity_type |
| samples.portions.slides.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.slides.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| samples.portions.slides.annotations.notes |  Open entry for any further description or characterization of the data
| samples.portions.slides.annotations.state |  The current state of the object
| samples.portions.slides.annotations.status |  Status of the annotation
| samples.portions.slides.annotations.submitter_id | Submitter supplied identifier information
| samples.portions.slides.annotations.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| summary.file_count |
| summary.file_size |
| summary.data_categories.data_category |
| summary.data_categories.file_count |
| summary.experimental_strategies.experimental_strategy |
| summary.experimental_strategies.file_count |
| tissue_source_site.bcr_id |
| tissue_source_site.code |
| tissue_source_site.name |
| tissue_source_site.project |
| tissue_source_site.tissue_source_site_id |


### File Fields

| Field Name |
| --- | ------ |
| access |
| acl |
| created_datetime |
| data_category |
| data_format |
| data_type |
| error_type |
| experimental_strategy |
| file_id |
| file_name |
| file_size |
| file_state |
| md5sum |
| origin |
| platform |
| revision |
| state |
| state_comment |
| submitter_id | Submitter supplied identifier information
| tags |
| type |
| updated_datetime |
| analysis.analysis_id |
| analysis.analysis_type |
| analysis.created_datetime |
| analysis.state |
| analysis.submitter_id | Submitter supplied identifier information
| analysis.updated_datetime |
| analysis.workflow_end_datetime |
| analysis.workflow_link |
| analysis.workflow_start_datetime |
| analysis.workflow_type |
| analysis.workflow_version |
| analysis.input_files.access |
| analysis.input_files.created_datetime |
| analysis.input_files.data_category |
| analysis.input_files.data_format |
| analysis.input_files.data_type |
| analysis.input_files.error_type |
| analysis.input_files.experimental_strategy |
| analysis.input_files.file_id |
| analysis.input_files.file_name |
| analysis.input_files.file_size |
| analysis.input_files.file_state |
| analysis.input_files.md5sum |
| analysis.input_files.platform |
| analysis.input_files.revision |
| analysis.input_files.state |
| analysis.input_files.state_comment |
| analysis.input_files.submitter_id | Submitter supplied identifier information
| analysis.input_files.updated_datetime |
| analysis.metadata.read_groups.adapter_name |
| analysis.metadata.read_groups.adapter_sequence |
| analysis.metadata.read_groups.base_caller_name |
| analysis.metadata.read_groups.base_caller_version |
| analysis.metadata.read_groups.created_datetime |
| analysis.metadata.read_groups.experiment_name |
| analysis.metadata.read_groups.flow_cell_barcode |
| analysis.metadata.read_groups.includes_spike_ins |
| analysis.metadata.read_groups.instrument_model |
| analysis.metadata.read_groups.is_paired_end |
| analysis.metadata.read_groups.library_name |
| analysis.metadata.read_groups.library_preparation_kit_catalog_number |
| analysis.metadata.read_groups.library_preparation_kit_name |
| analysis.metadata.read_groups.library_preparation_kit_vendor |
| analysis.metadata.read_groups.library_preparation_kit_version |
| analysis.metadata.read_groups.library_selection |
| analysis.metadata.read_groups.library_strand |
| analysis.metadata.read_groups.library_strategy |
| analysis.metadata.read_groups.platform |
| analysis.metadata.read_groups.read_group_id |
| analysis.metadata.read_groups.read_group_name |
| analysis.metadata.read_groups.read_length |
| analysis.metadata.read_groups.RIN |
| analysis.metadata.read_groups.sequencing_center |
| analysis.metadata.read_groups.sequencing_date |
| analysis.metadata.read_groups.size_selection_range |
| analysis.metadata.read_groups.spike_ins_concentration |
| analysis.metadata.read_groups.spike_ins_fasta |
| analysis.metadata.read_groups.state |
| analysis.metadata.read_groups.submitter_id | Submitter supplied identifier information
| analysis.metadata.read_groups.target_capture_kit_catalog_number |
| analysis.metadata.read_groups.target_capture_kit_name |
| analysis.metadata.read_groups.target_capture_kit_target_region |
| analysis.metadata.read_groups.target_capture_kit_vendor |
| analysis.metadata.read_groups.target_capture_kit_version |
| analysis.metadata.read_groups.to_trim_adapter_sequence |
| analysis.metadata.read_groups.updated_datetime |
| analysis.metadata.read_groups.read_group_qcs.adapter_content |
| analysis.metadata.read_groups.read_group_qcs.basic_statistics |
| analysis.metadata.read_groups.read_group_qcs.created_datetime |
| analysis.metadata.read_groups.read_group_qcs.encoding |
| analysis.metadata.read_groups.read_group_qcs.fastq_name |
| analysis.metadata.read_groups.read_group_qcs.kmer_content |
| analysis.metadata.read_groups.read_group_qcs.overrepresented_sequences |
| analysis.metadata.read_groups.read_group_qcs.per_base_n_content |
| analysis.metadata.read_groups.read_group_qcs.per_base_sequence_content |
| analysis.metadata.read_groups.read_group_qcs.per_base_sequence_quality |
| analysis.metadata.read_groups.read_group_qcs.per_sequence_gc_content |
| analysis.metadata.read_groups.read_group_qcs.per_sequence_quality_score |
| analysis.metadata.read_groups.read_group_qcs.per_tile_sequence_quality |
| analysis.metadata.read_groups.read_group_qcs.percent_gc_content |
| analysis.metadata.read_groups.read_group_qcs.read_group_qc_id |
| analysis.metadata.read_groups.read_group_qcs.sequence_duplication_levels |
| analysis.metadata.read_groups.read_group_qcs.sequence_length_distribution |
| analysis.metadata.read_groups.read_group_qcs.state |
| analysis.metadata.read_groups.read_group_qcs.submitter_id | Submitter supplied identifier information
| analysis.metadata.read_groups.read_group_qcs.total_sequences |
| analysis.metadata.read_groups.read_group_qcs.updated_datetime |
| analysis.metadata.read_groups.read_group_qcs.workflow_end_datetime |
| analysis.metadata.read_groups.read_group_qcs.workflow_link |
| analysis.metadata.read_groups.read_group_qcs.workflow_start_datetime |
| analysis.metadata.read_groups.read_group_qcs.workflow_type |
| analysis.metadata.read_groups.read_group_qcs.workflow_version |
| annotations.annotation_id |
| annotations.case_id |
| annotations.case_submitter_id | Submitter supplied identifier information
| annotations.category |  Characterization of the annotation
| annotations.classification |  Top level classification of the annotation
| annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| annotations.entity_id |
| annotations.entity_submitter_id | Submitter supplied identifier information
| annotations.entity_type |
| annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| annotations.notes |
| annotations.state |
| annotations.status |
| annotations.submitter_id | Submitter supplied identifier information
| annotations.updated_datetime |
| archive.archive_id |
| archive.created_datetime |
| archive.data_category |
| archive.data_format |
| archive.data_type |
| archive.error_type |
| archive.file_name |
| archive.file_size |
| archive.file_state |
| archive.md5sum |
| archive.revision |
| archive.state |
| archive.state_comment |
| archive.submitter_id | Submitter supplied identifier information
| archive.updated_datetime |
| associated_entities.case_id |
| associated_entities.entity_id |
| associated_entities.entity_submitter_id | Submitter supplied identifier information
| associated_entities.entity_type |
| cases.aliquot_ids |
| cases.analyte_ids |
| cases.case_id |
| cases.created_datetime |
| cases.days_to_index |
| cases.portion_ids |
| cases.sample_ids |
| cases.slide_ids |
| cases.state |
| cases.submitter_aliquot_ids |
| cases.submitter_analyte_ids |
| cases.submitter_id | Submitter supplied identifier information
| cases.submitter_portion_ids |
| cases.submitter_sample_ids |
| cases.submitter_slide_ids |
| cases.updated_datetime |
| cases.annotations.annotation_id |
| cases.annotations.case_id |
| cases.annotations.case_submitter_id | Submitter supplied identifier information
| cases.annotations.category |  Characterization of the annotation
| cases.annotations.classification |  Top level classification of the annotation
| cases.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.annotations.entity_id |
| cases.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.annotations.entity_type |
| cases.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.annotations.notes |
| cases.annotations.state |
| cases.annotations.status |
| cases.annotations.submitter_id | Submitter supplied identifier information
| cases.annotations.updated_datetime |
| cases.demographic.created_datetime |
| cases.demographic.demographic_id |
| cases.demographic.ethnicity |
| cases.demographic.gender |
| cases.demographic.race |
| cases.demographic.state |
| cases.demographic.submitter_id | Submitter supplied identifier information
| cases.demographic.updated_datetime |
| cases.demographic.year_of_birth |
| cases.demographic.year_of_death |
| cases.diagnoses.age_at_diagnosis |
| cases.diagnoses.classification_of_tumor |
| cases.diagnoses.created_datetime |
| cases.diagnoses.days_to_birth |
| cases.diagnoses.days_to_death |
| cases.diagnoses.days_to_last_follow_up |
| cases.diagnoses.days_to_last_known_disease_status |
| cases.diagnoses.days_to_recurrence |
| cases.diagnoses.diagnosis_id |
| cases.diagnoses.last_known_disease_status |
| cases.diagnoses.morphology |
| cases.diagnoses.primary_diagnosis |
| cases.diagnoses.prior_malignancy |
| cases.diagnoses.progression_or_recurrence |
| cases.diagnoses.site_of_resection_or_biopsy |
| cases.diagnoses.state |
| cases.diagnoses.submitter_id | Submitter supplied identifier information
| cases.diagnoses.tissue_or_organ_of_origin |
| cases.diagnoses.tumor_grade |
| cases.diagnoses.tumor_stage |
| cases.diagnoses.updated_datetime |
| cases.diagnoses.vital_status |
| cases.diagnoses.treatments.created_datetime |
| cases.diagnoses.treatments.days_to_treatment |
| cases.diagnoses.treatments.state |
| cases.diagnoses.treatments.submitter_id | Submitter supplied identifier information
| cases.diagnoses.treatments.therapeutic_agents |
| cases.diagnoses.treatments.treatment_id |
| cases.diagnoses.treatments.treatment_intent_type |
| cases.diagnoses.treatments.treatment_or_therapy |
| cases.diagnoses.treatments.updated_datetime |
| cases.exposures.alcohol_history |
| cases.exposures.alcohol_intensity |
| cases.exposures.bmi |
| cases.exposures.cigarettes_per_day |
| cases.exposures.created_datetime |
| cases.exposures.exposure_id |
| cases.exposures.height |
| cases.exposures.state |
| cases.exposures.submitter_id | Submitter supplied identifier information
| cases.exposures.updated_datetime |
| cases.exposures.weight |
| cases.exposures.years_smoked |
| cases.family_histories.created_datetime |
| cases.family_histories.family_history_id |
| cases.family_histories.relationship_age_at_diagnosis |
| cases.family_histories.relationship_gender |
| cases.family_histories.relationship_primary_diagnosis |
| cases.family_histories.relationship_type |
| cases.family_histories.relative_with_cancer_history |
| cases.family_histories.state |
| cases.family_histories.submitter_id | Submitter supplied identifier information
| cases.family_histories.updated_datetime |
| cases.files.created_datetime |
| cases.files.error_type |
| cases.files.file_id |
| cases.files.file_name |
| cases.files.file_size |
| cases.files.file_state |
| cases.files.md5sum |
| cases.files.state |
| cases.files.state_comment |
| cases.files.submitter_id | Submitter supplied identifier information
| cases.files.updated_datetime |
| cases.project.dbgap_accession_number |
| cases.project.disease_type |
| cases.project.name |
| cases.project.primary_site |
| cases.project.project_id |
| cases.project.released |
| cases.project.state |
| cases.project.program.dbgap_accession_number |
| cases.project.program.name |
| cases.project.program.program_id |
| cases.samples.composition |
| cases.samples.created_datetime |
| cases.samples.current_weight |
| cases.samples.days_to_collection |
| cases.samples.days_to_sample_procurement |
| cases.samples.freezing_method |
| cases.samples.initial_weight |
| cases.samples.intermediate_dimension |
| cases.samples.is_ffpe |
| cases.samples.longest_dimension |
| cases.samples.oct_embedded |
| cases.samples.pathology_report_uuid |
| cases.samples.preservation_method |  Text term that represents the method used to preserve the sample
| cases.samples.sample_id |
| cases.samples.sample_type |  Text term to describe the source of a biospecimen used for a laboratory test
| cases.samples.sample_type_id |  The accompanying sample type id for the sample type
| cases.samples.shortest_dimension |  Numeric value that represents the shortest dimension of the sample, measured in millimeters
| cases.samples.state |
| cases.samples.submitter_id | Submitter supplied identifier information
| cases.samples.time_between_clamping_and_freezing |
| cases.samples.time_between_excision_and_freezing |  Numeric representation of the elapsed time between the excision and freezing of the sample, measured in minutes
| cases.samples.tissue_type |  Text term that represents a description of the kind of tissue collected with respect to disease status or proximity to tumor tissue
| cases.samples.tumor_code |  Diagnostic tumor code of the tissue sample source
| cases.samples.tumor_code_id |  BCR-defined id code for the tumor sample
| cases.samples.tumor_descriptor |  Text that describes the kind of disease present in the tumor specimen as related to a specific timepoint
| cases.samples.updated_datetime |
| cases.samples.annotations.annotation_id |
| cases.samples.annotations.case_id |
| cases.samples.annotations.case_submitter_id | Submitter supplied identifier information
| cases.samples.annotations.category | Top level characterization of the annotation
| cases.samples.annotations.classification |  Top level classification of the annotation
| cases.samples.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.samples.annotations.entity_id |
| cases.samples.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.samples.annotations.entity_type |
| cases.samples.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.annotations.notes |
| cases.samples.annotations.state |
| cases.samples.annotations.status |
| cases.samples.annotations.submitter_id | Submitter supplied identifier information
| cases.samples.annotations.updated_datetime |
| cases.samples.portions.created_datetime |
| cases.samples.portions.creation_datetime |
| cases.samples.portions.is_ffpe |
| cases.samples.portions.portion_id |
| cases.samples.portions.portion_number |  Numeric value that represents the sequential number assigned to a portion of the sample.
| cases.samples.portions.state |  The current state of the object
| cases.samples.portions.submitter_id |  The legacy barcode used before prior to the use UUIDs, varies by project. For TCGA this is bcrportionbarcode
| cases.samples.portions.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]\
| cases.samples.portions.weight |  Numeric value that represents the sample portion weight, measured in milligrams
| cases.samples.portions.analytes.a260_a280_ratio |
| cases.samples.portions.analytes.amount |
| cases.samples.portions.analytes.analyte_id |
| cases.samples.portions.analytes.analyte_type |
| cases.samples.portions.analytes.analyte_type_id |
| cases.samples.portions.analytes.concentration |
| cases.samples.portions.analytes.created_datetime |
| cases.samples.portions.analytes.spectrophotometer_method |
| cases.samples.portions.analytes.state |
| cases.samples.portions.analytes.submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.updated_datetime |
| cases.samples.portions.analytes.well_number |
| cases.samples.portions.analytes.aliquots.aliquot_id |
| cases.samples.portions.analytes.aliquots.amount |
| cases.samples.portions.analytes.aliquots.analyte_type |
| cases.samples.portions.analytes.aliquots.analyte_type_id |
| cases.samples.portions.analytes.aliquots.concentration |
| cases.samples.portions.analytes.aliquots.created_datetime |
| cases.samples.portions.analytes.aliquots.source_center |
| cases.samples.portions.analytes.aliquots.state |
| cases.samples.portions.analytes.aliquots.submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.aliquots.updated_datetime |
| cases.samples.portions.analytes.aliquots.annotations.annotation_id |
| cases.samples.portions.analytes.aliquots.annotations.case_id |
| cases.samples.portions.analytes.aliquots.annotations.case_submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.aliquots.annotations.category |  Top level characterization of the annotation
| cases.samples.portions.analytes.aliquots.annotations.classification |  Top level classification of the annotation
| cases.samples.portions.analytes.aliquots.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.aliquots.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.samples.portions.analytes.aliquots.annotations.entity_id |
| cases.samples.portions.analytes.aliquots.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.aliquots.annotations.entity_type |
| cases.samples.portions.analytes.aliquots.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.aliquots.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.aliquots.annotations.notes |
| cases.samples.portions.analytes.aliquots.annotations.state |
| cases.samples.portions.analytes.aliquots.annotations.status |
| cases.samples.portions.analytes.aliquots.annotations.submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.aliquots.annotations.updated_datetime |
| cases.samples.portions.analytes.aliquots.center.center_id |
| cases.samples.portions.analytes.aliquots.center.center_type |
| cases.samples.portions.analytes.aliquots.center.code |  Numeric code for the center
| cases.samples.portions.analytes.aliquots.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| cases.samples.portions.analytes.aliquots.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| cases.samples.portions.analytes.aliquots.center.short_name |  Shortened name of the center (e.g. BI)
| cases.samples.portions.analytes.annotations.annotation_id |
| cases.samples.portions.analytes.annotations.case_id |
| cases.samples.portions.analytes.annotations.case_submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.annotations.category |  Top level characterization of the annotation
| cases.samples.portions.analytes.annotations.classification |  Top level classification of the annotation
| cases.samples.portions.analytes.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.samples.portions.analytes.annotations.entity_id |
| cases.samples.portions.analytes.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.annotations.entity_type |
| cases.samples.portions.analytes.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.analytes.annotations.notes |
| cases.samples.portions.analytes.annotations.state |
| cases.samples.portions.analytes.annotations.status |
| cases.samples.portions.analytes.annotations.submitter_id | Submitter supplied identifier information
| cases.samples.portions.analytes.annotations.updated_datetime |
| cases.samples.portions.annotations.annotation_id |
| cases.samples.portions.annotations.case_id |
| cases.samples.portions.annotations.case_submitter_id | Submitter supplied identifier information
| cases.samples.portions.annotations.category |  Top level characterization of the annotation
| cases.samples.portions.annotations.classification |  Top level classification of the annotation
| cases.samples.portions.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.samples.portions.annotations.entity_id |
| cases.samples.portions.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.samples.portions.annotations.entity_type |
| cases.samples.portions.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.annotations.notes |
| cases.samples.portions.annotations.state |
| cases.samples.portions.annotations.status |
| cases.samples.portions.annotations.submitter_id | Submitter supplied identifier information
| cases.samples.portions.annotations.updated_datetime |
| cases.samples.portions.center.center_id |
| cases.samples.portions.center.center_type |
| cases.samples.portions.center.code |  Numeric code for the center
| cases.samples.portions.center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)  
| cases.samples.portions.center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| cases.samples.portions.center.short_name |  Shortened name of the center (e.g. BI)
| cases.samples.portions.slides.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.slides.number_proliferating_cells |  Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s).
| cases.samples.portions.slides.percent_eosinophil_infiltration |  Numeric value that represents the count of proliferating cells determined during pathologic review of the sample slide(s).
| cases.samples.portions.slides.percent_granulocyte_infiltration |  Numeric value to represent the percentage of infiltration by granulocytes in a tumor sample or specimen
| cases.samples.portions.slides.percent_inflam_infiltration |  Numeric value to represent local response to cellular injury, marked by capillary dilatation, edema and leukocyte infiltration; clinically, inflammation is manifest by reddness, heat, pain, swelling and loss of function, with the need to heal damaged tissue
| cases.samples.portions.slides.percent_lymphocyte_infiltration |  Numeric value to represent the percentage of infiltration by lymphocytes in a solid tissue normal sample or specimen
| cases.samples.portions.slides.percent_monocyte_infiltration |  Numeric value to represent the percentage of monocyte infiltration in a sample or specimen
| cases.samples.portions.slides.percent_necrosis |  Numeric value to represent the percentage of cell death in a malignant tumor sample or specimen
| cases.samples.portions.slides.percent_neutrophil_infiltration |  Numeric value to represent the percentage of infiltration by neutrophils in a tumor sample or specimen
| cases.samples.portions.slides.percent_normal_cells |  Numeric value to represent the percentage of normal cell content in a malignant tumor sample or specimen
| cases.samples.portions.slides.percent_stromal_cells |  Numeric value to represent the percentage of reactive cells that are present in a malignant tumor sample or specimen but are not malignant such as fibroblasts, vascular structures, etc.\
| cases.samples.portions.slides.percent_tumor_cells |  Numeric value that represents the percentage of infiltration by granulocytes in a sample
| cases.samples.portions.slides.percent_tumor_nuclei |  Numeric value to represent the percentage of tumor nuclei in a malignant neoplasm sample or specimen
| cases.samples.portions.slides.section_location |  Tissue source of the slide
| cases.samples.portions.slides.slide_id |
| cases.samples.portions.slides.state |  The current state of the object
| cases.samples.portions.slides.submitter_id |  The legacy barcode used before prior to the use UUIDs, varies by project
| cases.samples.portions.slides.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]\
| cases.samples.portions.slides.annotations.annotation_id |
| cases.samples.portions.slides.annotations.case_id |
| cases.samples.portions.slides.annotations.case_submitter_id | Submitter supplied identifier information
| cases.samples.portions.slides.annotations.category |  Top level characterization of the annotation
| cases.samples.portions.slides.annotations.classification |  Top level classification of the annotation
| cases.samples.portions.slides.annotations.created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.slides.annotations.creator |  Name of the person or entity responsible for the creation of the annotation
| cases.samples.portions.slides.annotations.entity_id |
| cases.samples.portions.slides.annotations.entity_submitter_id | Submitter supplied identifier information
| cases.samples.portions.slides.annotations.entity_type |
| cases.samples.portions.slides.annotations.legacy_created_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.slides.annotations.legacy_updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.samples.portions.slides.annotations.notes |  Open entry for any further description or characterization of the data
| cases.samples.portions.slides.annotations.state |  The current state of the object
| cases.samples.portions.slides.annotations.status |  Status of the annotation
| cases.samples.portions.slides.annotations.submitter_id | Submitter supplied identifier information
| cases.samples.portions.slides.annotations.updated_datetime |  A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]
| cases.summary.file_count |
| cases.summary.file_size |
| cases.summary.data_categories.data_category |
| cases.summary.data_categories.file_count |
| cases.summary.experimental_strategies.experimental_strategy |
| cases.summary.experimental_strategies.file_count |
| cases.tissue_source_site.bcr_id |  TCGA-provided BCR id
| cases.tissue_source_site.code |  TCGA-provided TSS code
| cases.tissue_source_site.name |  Name of the source site
| cases.tissue_source_site.project |  Study name of the project
| cases.tissue_source_site.tissue_source_site_id |
| center.center_id |
| center.center_type |
| center.code |  Numeric code for the center
| center.name |  Name of the center (e.g. Center For Data Intensive Science at the University of Chicago)
| center.namespace |  Domain name of the center (e.g. cdis.uchicago.edu)
| center.short_name |  Shortened name of the center (e.g. BI)
| downstream_analyses.analysis_id |
| downstream_analyses.analysis_type |
| downstream_analyses.created_datetime |
| downstream_analyses.state |
| downstream_analyses.submitter_id | Submitter supplied identifier information
| downstream_analyses.updated_datetime |
| downstream_analyses.workflow_end_datetime |
| downstream_analyses.workflow_link |
| downstream_analyses.workflow_start_datetime |
| downstream_analyses.workflow_type |
| downstream_analyses.workflow_version |
| downstream_analyses.output_files.access |
| downstream_analyses.output_files.created_datetime |
| downstream_analyses.output_files.data_category |
| downstream_analyses.output_files.data_format |
| downstream_analyses.output_files.data_type |
| downstream_analyses.output_files.error_type |
| downstream_analyses.output_files.experimental_strategy |
| downstream_analyses.output_files.file_id |
| downstream_analyses.output_files.file_name |
| downstream_analyses.output_files.file_size |
| downstream_analyses.output_files.file_state |
| downstream_analyses.output_files.md5sum |
| downstream_analyses.output_files.platform |
| downstream_analyses.output_files.revision |
| downstream_analyses.output_files.state |
| downstream_analyses.output_files.state_comment |
| downstream_analyses.output_files.submitter_id | Submitter supplied identifier information
| downstream_analyses.output_files.updated_datetime |
| index_files.access |
| index_files.created_datetime |
| index_files.data_category |
| index_files.data_format |
| index_files.data_type |
| index_files.error_type |
| index_files.experimental_strategy |
| index_files.file_id |
| index_files.file_name |
| index_files.file_size |
| index_files.file_state |
| index_files.md5sum |
| index_files.platform |
| index_files.revision |
| index_files.state |
| index_files.state_comment |
| index_files.submitter_id | Submitter supplied identifier information
| index_files.updated_datetime |
| metadata_files.access |
| metadata_files.created_datetime |
| metadata_files.data_category |
| metadata_files.data_format |
| metadata_files.data_type |
| metadata_files.error_type |
| metadata_files.file_id |
| metadata_files.file_name |
| metadata_files.file_size |
| metadata_files.file_state |
| metadata_files.md5sum |
| metadata_files.state |
| metadata_files.state_comment |
| metadata_files.submitter_id | Submitter supplied identifier information
| metadata_files.type |
| metadata_files.updated_datetime |



### Annotation Fields


| Field Name |
| --- |
| annotation_id |
| case_id |
| case_submitter_id | Submitter supplied identifier information
| category |
| classification |
| created_datetime |
| entity_id |
| entity_submitter_id | Submitter supplied identifier information
| entity_type |
| legacy_created_datetime |
| legacy_updated_datetime |
| notes |
| state |
| status |
| submitter_id | Submitter supplied identifier information
| updated_datetime |
| project.code |
| project.dbgap_accession_number |
| project.disease_type |
| project.name |
| project.primary_site |
| project.program.dbgap_accession_number |
| project.program.name |
| project.program.program_id |
| project.project_id |
| project.released |
| project.state |

## Field Group Listing by Endpoint

### Projects Field Groups

| Field Group Name |
| --- |
| program |
| summary |
| summary.data_categories |
| summary.experimental_strategies |

### Cases Field Groups

| Field Group Name |
| --- |
| annotations |
| demographic |
| diagnoses |
| diagnoses.treatments |
| exposures |
| family_histories |
| files |
| files.analysis |
| files.analysis.input_files |
| files.analysis.metadata |
| files.analysis.metadata.read_groups |
| files.analysis.metadata.read_groups.read_group_qcs |
| files.archive |
| files.cases |
| files.cases.annotations |
| files.cases.demographic |
| files.cases.diagnoses |
| files.cases.diagnoses.treatments |
| files.cases.exposures |
| files.cases.family_histories |
| files.cases.files |
| files.cases.project |
| files.cases.project.program |
| files.cases.samples |
| files.cases.samples.annotations |
| files.cases.samples.portions |
| files.cases.samples.portions.analytes |
| files.cases.samples.portions.analytes.aliquots |
| files.cases.samples.portions.analytes.aliquots.annotations |
| files.cases.samples.portions.analytes.aliquots.center |
| files.cases.samples.portions.analytes.annotations |
| files.cases.samples.portions.annotations |
| files.cases.samples.portions.center |
| files.cases.samples.portions.slides |
| files.cases.samples.portions.slides.annotations |
| files.cases.summary |
| files.cases.summary.data_categories |
| files.cases.summary.experimental_strategies |
| files.cases.tissue_source_site |
| files.center |
| files.downstream_analyses |
| files.downstream_analyses.output_files |
| files.index_files |
| files.metadata_files |
| project |
| project.program |
| samples |
| samples.annotations |
| samples.portions |
| samples.portions.analytes |
| samples.portions.analytes.aliquots |
| samples.portions.analytes.aliquots.annotations |
| samples.portions.analytes.aliquots.center |
| samples.portions.analytes.annotations |
| samples.portions.annotations |
| samples.portions.center |
| samples.portions.slides |
| samples.portions.slides.annotations |
| summary |
| summary.data_categories |
| summary.experimental_strategies |
| tissue_source_site |

### Files Field Groups

| Field Group Name |
| --- |
| analysis |
| analysis.input_files |
| analysis.metadata |
| analysis.metadata.read_groups |
| analysis.metadata.read_groups.read_group_qcs |
| annotations |
| archive |
| associated_entities |
| cases |
| cases.annotations |
| cases.demographic |
| cases.diagnoses |
| cases.diagnoses.treatments |
| cases.exposures |
| cases.family_histories |
| cases.files |
| cases.project |
| cases.project.program |
| cases.samples |
| cases.samples.annotations |
| cases.samples.portions |
| cases.samples.portions.analytes |
| cases.samples.portions.analytes.aliquots |
| cases.samples.portions.analytes.aliquots.annotations |
| cases.samples.portions.analytes.aliquots.center |
| cases.samples.portions.analytes.annotations |
| cases.samples.portions.annotations |
| cases.samples.portions.center |
| cases.samples.portions.slides |
| cases.samples.portions.slides.annotations |
| cases.summary |
| cases.summary.data_categories |
| cases.summary.experimental_strategies |
| cases.tissue_source_site |
| center |
| downstream_analyses |
| downstream_analyses.output_files |
| index_files |
| metadata_files |

### Annotations Field Groups

| Field Group Name |
| --- |
| project |
| project.program |
