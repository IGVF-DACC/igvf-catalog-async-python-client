# igvf-catalog-async-client

Asyncio client for the [IGVF Catalog API](https://api.catalogkg.igvf.org/), built on `aiohttp`.

IGVF Catalog OpenAPI compliant REST API built using tRPC with Express.

Our database uses 0-based, half-open coordinates for genomic coordinates in the GRCh38 (human) and GRCm39 (mouse) reference genomes.

Data is licensed under the <a href=https://creativecommons.org/licenses/by/4.0/ target=\"_blank\">Creative Commons license</a> and the software is licensed under the <a href=https://spdx.org/licenses/MIT.html target=\"_blank\">MIT license</a>.

- API version: 1.3.1.dev20261030174037
- Package version: 1.3.1.dev20261030174037
- Generator version: 7.14.0

This package is generated with [OpenAPI Generator](https://openapi-generator.tech) by
[igvf-catalog-client-openapi-spec](https://github.com/IGVF-DACC/igvf-catalog-client-openapi-spec)
whenever the IGVF Catalog changes. Don't edit generated files by hand; change
`templates/` here or the pipeline in that repo instead.

## Requirements

Python 3.9+

## Installation

Releases follow IGVF Catalog releases and are published to PyPI:

```sh
pip install igvf-catalog-async-client
```

Development builds track the catalog's `dev` branch and are installed from this repo's `dev` branch:

```sh
pip install "git+https://github.com/IGVF-DACC/igvf-catalog-async-python-client.git@dev"
```

The default host is the API the package was generated against: releases use
`https://api.catalogkg.igvf.org/api` and dev builds use
`https://catalog-api-dev.demo.igvf.org/api`. Pass `Configuration(host=...)` to use another.

## Quick start

```python
import asyncio

import igvf_catalog_async_client

configuration = igvf_catalog_async_client.Configuration(host="https://api.catalogkg.igvf.org/api")


async def main():
    async with igvf_catalog_async_client.ApiClient(configuration) as api_client:
        api = igvf_catalog_async_client.AsyncIgvfCatalogApi(api_client)
        genes = await api.genes(name="ATF3")
        print(genes[0].to_dict())


asyncio.run(main())
```

Every endpoint is a method on `AsyncIgvfCatalogApi`, listed below. The interactive API documentation is at
[api.catalogkg.igvf.org](https://api.catalogkg.igvf.org/).

## Getting Started

```python

import igvf_catalog_async_client
from igvf_catalog_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://catalog-api-dev.demo.igvf.org/api
# See configuration.py for a list of all supported configuration parameters.
configuration = igvf_catalog_async_client.Configuration(
    host = "https://catalog-api-dev.demo.igvf.org/api"
)



# Enter a context with an instance of the API client
async with igvf_catalog_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = igvf_catalog_async_client.AsyncIgvfCatalogApi(api_client)
    gene_id = 'gene_id_example' # str | 
    dataset = 'dataset_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 3.4 # float |  (optional)

    try:
        api_response = await api_instance.all_coding_variants_from_genes(gene_id, dataset, page=page, limit=limit)
        print("The response of AsyncIgvfCatalogApi->all_coding_variants_from_genes:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AsyncIgvfCatalogApi->all_coding_variants_from_genes: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://catalog-api-dev.demo.igvf.org/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AsyncIgvfCatalogApi* | [**variants**](docs/AsyncIgvfCatalogApi.md#variants) | **GET** /variants | 
*AsyncIgvfCatalogApi* | [**coding_variants**](docs/AsyncIgvfCatalogApi.md#coding_variants) | **GET** /coding-variants | 
*AsyncIgvfCatalogApi* | [**genomic_elements**](docs/AsyncIgvfCatalogApi.md#genomic_elements) | **GET** /genomic-elements | 
*AsyncIgvfCatalogApi* | [**genes**](docs/AsyncIgvfCatalogApi.md#genes) | **GET** /genes | 
*AsyncIgvfCatalogApi* | [**genes_structure**](docs/AsyncIgvfCatalogApi.md#genes_structure) | **GET** /genes-structure | 
*AsyncIgvfCatalogApi* | [**transcripts**](docs/AsyncIgvfCatalogApi.md#transcripts) | **GET** /transcripts | 
*AsyncIgvfCatalogApi* | [**proteins**](docs/AsyncIgvfCatalogApi.md#proteins) | **GET** /proteins | 
*AsyncIgvfCatalogApi* | [**complexes**](docs/AsyncIgvfCatalogApi.md#complexes) | **GET** /complexes | 
*AsyncIgvfCatalogApi* | [**pathways**](docs/AsyncIgvfCatalogApi.md#pathways) | **GET** /pathways | 
*AsyncIgvfCatalogApi* | [**motifs**](docs/AsyncIgvfCatalogApi.md#motifs) | **GET** /motifs | 
*AsyncIgvfCatalogApi* | [**drugs**](docs/AsyncIgvfCatalogApi.md#drugs) | **GET** /drugs | 
*AsyncIgvfCatalogApi* | [**ontology_term**](docs/AsyncIgvfCatalogApi.md#ontology_term) | **GET** /ontology-terms | 
*AsyncIgvfCatalogApi* | [**studies**](docs/AsyncIgvfCatalogApi.md#studies) | **GET** /studies | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_variants**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_variants) | **GET** /variants/genomic-elements | 
*AsyncIgvfCatalogApi* | [**genes_from_variants**](docs/AsyncIgvfCatalogApi.md#genes_from_variants) | **GET** /variants/genes | 
*AsyncIgvfCatalogApi* | [**proteins_from_variants**](docs/AsyncIgvfCatalogApi.md#proteins_from_variants) | **GET** /variants/proteins | 
*AsyncIgvfCatalogApi* | [**phenotypes_from_variants**](docs/AsyncIgvfCatalogApi.md#phenotypes_from_variants) | **GET** /variants/phenotypes | 
*AsyncIgvfCatalogApi* | [**biosamples_from_variants**](docs/AsyncIgvfCatalogApi.md#biosamples_from_variants) | **GET** /variants/biosamples | 
*AsyncIgvfCatalogApi* | [**variants_from_proteins**](docs/AsyncIgvfCatalogApi.md#variants_from_proteins) | **GET** /proteins/variants | 
*AsyncIgvfCatalogApi* | [**proteins_proteins**](docs/AsyncIgvfCatalogApi.md#proteins_proteins) | **GET** /proteins/proteins | 
*AsyncIgvfCatalogApi* | [**variants_from_phenotypes**](docs/AsyncIgvfCatalogApi.md#variants_from_phenotypes) | **GET** /phenotypes/variants | 
*AsyncIgvfCatalogApi* | [**coding_variants_from_phenotypes**](docs/AsyncIgvfCatalogApi.md#coding_variants_from_phenotypes) | **GET** /phenotypes/coding-variants | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_phenotypes**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_phenotypes) | **GET** /phenotypes/genomic-elements | 
*AsyncIgvfCatalogApi* | [**variants_from_genomic_elements**](docs/AsyncIgvfCatalogApi.md#variants_from_genomic_elements) | **GET** /genomic-elements/variants | 
*AsyncIgvfCatalogApi* | [**genes_from_genomic_elements**](docs/AsyncIgvfCatalogApi.md#genes_from_genomic_elements) | **GET** /genomic-elements/genes | 
*AsyncIgvfCatalogApi* | [**phenotypes_from_genomic_elements**](docs/AsyncIgvfCatalogApi.md#phenotypes_from_genomic_elements) | **GET** /genomic-elements/phenotypes | 
*AsyncIgvfCatalogApi* | [**biosamples_from_genomic_elements**](docs/AsyncIgvfCatalogApi.md#biosamples_from_genomic_elements) | **GET** /genomic-elements/biosamples | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_genomic_elements**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_genomic_elements) | **GET** /genomic-elements/genomic-elements | 
*AsyncIgvfCatalogApi* | [**variants_from_genes**](docs/AsyncIgvfCatalogApi.md#variants_from_genes) | **GET** /genes/variants | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_genes**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_genes) | **GET** /genes/genomic-elements | 
*AsyncIgvfCatalogApi* | [**phenotypes_from_coding_variants**](docs/AsyncIgvfCatalogApi.md#phenotypes_from_coding_variants) | **GET** /coding-variants/phenotypes | 
*AsyncIgvfCatalogApi* | [**variants_from_biosamples**](docs/AsyncIgvfCatalogApi.md#variants_from_biosamples) | **GET** /biosamples/variants | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_biosamples**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_biosamples) | **GET** /biosamples/genomic-elements | 
*AsyncIgvfCatalogApi* | [**variant_by_frequency_source**](docs/AsyncIgvfCatalogApi.md#variant_by_frequency_source) | **GET** /variants/freq | 
*AsyncIgvfCatalogApi* | [**grn**](docs/AsyncIgvfCatalogApi.md#grn) | **GET** /gene-regulatory-network | 
*AsyncIgvfCatalogApi* | [**enhancer_gene_predictions**](docs/AsyncIgvfCatalogApi.md#enhancer_gene_predictions) | **GET** /enhancer-gene-predictions | 
*AsyncIgvfCatalogApi* | [**qtls**](docs/AsyncIgvfCatalogApi.md#qtls) | **GET** /qtls | 
*AsyncIgvfCatalogApi* | [**variant_summary**](docs/AsyncIgvfCatalogApi.md#variant_summary) | **GET** /variants/summary | 
*AsyncIgvfCatalogApi* | [**variants_from_variant_id_summary**](docs/AsyncIgvfCatalogApi.md#variants_from_variant_id_summary) | **GET** /variants/variant-ld/summary | 
*AsyncIgvfCatalogApi* | [**variants_region_summary**](docs/AsyncIgvfCatalogApi.md#variants_region_summary) | **GET** /variants/region-summary | 
*AsyncIgvfCatalogApi* | [**qtl_summary_endpoint**](docs/AsyncIgvfCatalogApi.md#qtl_summary_endpoint) | **GET** /variants/genes/summary | 
*AsyncIgvfCatalogApi* | [**genomic_elements_from_variants_count**](docs/AsyncIgvfCatalogApi.md#genomic_elements_from_variants_count) | **GET** /variants/predictions-count | 
*AsyncIgvfCatalogApi* | [**predictions_from_variants**](docs/AsyncIgvfCatalogApi.md#predictions_from_variants) | **GET** /variants/predictions | 
*AsyncIgvfCatalogApi* | [**deprecated_coding_variants_summary**](docs/AsyncIgvfCatalogApi.md#deprecated_coding_variants_summary) | **GET** /variants/phenotypes/score-summary | 
*AsyncIgvfCatalogApi* | [**deprecated_nearest_genes**](docs/AsyncIgvfCatalogApi.md#deprecated_nearest_genes) | **GET** /variants/nearest-genes | 
*AsyncIgvfCatalogApi* | [**variants_alleles**](docs/AsyncIgvfCatalogApi.md#variants_alleles) | **GET** /variants/gnomad-alleles | 
*AsyncIgvfCatalogApi* | [**variants_genomic_elements_genes**](docs/AsyncIgvfCatalogApi.md#variants_genomic_elements_genes) | **GET** /variants/genomic-elements/genes | 
*AsyncIgvfCatalogApi* | [**genomic_elements_predictions_from_variant**](docs/AsyncIgvfCatalogApi.md#genomic_elements_predictions_from_variant) | **GET** /variants/genomic-elements/cell-gene-predictions | 
*AsyncIgvfCatalogApi* | [**genes_proteins_from_variants**](docs/AsyncIgvfCatalogApi.md#genes_proteins_from_variants) | **GET** /variants/genes-proteins | 
*AsyncIgvfCatalogApi* | [**coding_variants_from_genes**](docs/AsyncIgvfCatalogApi.md#coding_variants_from_genes) | **GET** /genes/coding-variants/scores | 
*AsyncIgvfCatalogApi* | [**all_coding_variants_from_genes**](docs/AsyncIgvfCatalogApi.md#all_coding_variants_from_genes) | **GET** /genes/coding-variants/all-scores | 
*AsyncIgvfCatalogApi* | [**variants_from_gene_proteins**](docs/AsyncIgvfCatalogApi.md#variants_from_gene_proteins) | **GET** /genes-proteins/variants | 
*AsyncIgvfCatalogApi* | [**genes_proteins_genes_proteins**](docs/AsyncIgvfCatalogApi.md#genes_proteins_genes_proteins) | **GET** /genes-proteins/genes-proteins | 
*AsyncIgvfCatalogApi* | [**coding_variants_summary**](docs/AsyncIgvfCatalogApi.md#coding_variants_summary) | **GET** /coding-variants/phenotypes/score-summary | 
*AsyncIgvfCatalogApi* | [**coding_variants_count_from_gene**](docs/AsyncIgvfCatalogApi.md#coding_variants_count_from_gene) | **GET** /coding-variants/phenotypes-count | 
*AsyncIgvfCatalogApi* | [**ontology_term_parents**](docs/AsyncIgvfCatalogApi.md#ontology_term_parents) | **GET** /ontology-terms/{ontology_term_id}/parents | 
*AsyncIgvfCatalogApi* | [**ontology_term_children**](docs/AsyncIgvfCatalogApi.md#ontology_term_children) | **GET** /ontology-terms/{ontology_term_id}/children | 
*AsyncIgvfCatalogApi* | [**ontology_term_transitive_closure**](docs/AsyncIgvfCatalogApi.md#ontology_term_transitive_closure) | **GET** /ontology-terms/{ontology_term_id_start}/transitive-closure/{ontology_term_id_end} | 
*AsyncIgvfCatalogApi* | [**variants_from_variant_id**](docs/AsyncIgvfCatalogApi.md#variants_from_variant_id) | **GET** /variants/variant-ld | 
*AsyncIgvfCatalogApi* | [**coding_variants_from_variants**](docs/AsyncIgvfCatalogApi.md#coding_variants_from_variants) | **GET** /variants/coding-variants | 
*AsyncIgvfCatalogApi* | [**drugs_from_variants**](docs/AsyncIgvfCatalogApi.md#drugs_from_variants) | **GET** /variants/drugs | 
*AsyncIgvfCatalogApi* | [**disease_from_variants**](docs/AsyncIgvfCatalogApi.md#disease_from_variants) | **GET** /variants/diseases | 
*AsyncIgvfCatalogApi* | [**variants_from_coding_variants**](docs/AsyncIgvfCatalogApi.md#variants_from_coding_variants) | **GET** /coding-variants/variants | 
*AsyncIgvfCatalogApi* | [**transcripts_from_genes**](docs/AsyncIgvfCatalogApi.md#transcripts_from_genes) | **GET** /genes/transcripts | 
*AsyncIgvfCatalogApi* | [**genes_transcripts_genes**](docs/AsyncIgvfCatalogApi.md#genes_transcripts_genes) | **GET** /genes/transcripts/genes | 
*AsyncIgvfCatalogApi* | [**proteins_from_genes**](docs/AsyncIgvfCatalogApi.md#proteins_from_genes) | **GET** /genes/proteins | 
*AsyncIgvfCatalogApi* | [**pathways_from_genes**](docs/AsyncIgvfCatalogApi.md#pathways_from_genes) | **GET** /genes/pathways | 
*AsyncIgvfCatalogApi* | [**genes_genes**](docs/AsyncIgvfCatalogApi.md#genes_genes) | **GET** /genes/genes | 
*AsyncIgvfCatalogApi* | [**diseases_from_genes**](docs/AsyncIgvfCatalogApi.md#diseases_from_genes) | **GET** /genes/diseases | 
*AsyncIgvfCatalogApi* | [**genes_from_transcripts**](docs/AsyncIgvfCatalogApi.md#genes_from_transcripts) | **GET** /transcripts/genes | 
*AsyncIgvfCatalogApi* | [**proteins_from_transcripts**](docs/AsyncIgvfCatalogApi.md#proteins_from_transcripts) | **GET** /transcripts/proteins | 
*AsyncIgvfCatalogApi* | [**transcripts_from_proteins**](docs/AsyncIgvfCatalogApi.md#transcripts_from_proteins) | **GET** /proteins/transcripts | 
*AsyncIgvfCatalogApi* | [**genes_from_proteins**](docs/AsyncIgvfCatalogApi.md#genes_from_proteins) | **GET** /proteins/genes | 
*AsyncIgvfCatalogApi* | [**complexes_from_proteins**](docs/AsyncIgvfCatalogApi.md#complexes_from_proteins) | **GET** /proteins/complexes | 
*AsyncIgvfCatalogApi* | [**proteins_from_complexes**](docs/AsyncIgvfCatalogApi.md#proteins_from_complexes) | **GET** /complexes/proteins | 
*AsyncIgvfCatalogApi* | [**motifs_from_proteins**](docs/AsyncIgvfCatalogApi.md#motifs_from_proteins) | **GET** /proteins/motifs | 
*AsyncIgvfCatalogApi* | [**proteins_from_motifs**](docs/AsyncIgvfCatalogApi.md#proteins_from_motifs) | **GET** /motifs/proteins | 
*AsyncIgvfCatalogApi* | [**genes_from_pathways**](docs/AsyncIgvfCatalogApi.md#genes_from_pathways) | **GET** /pathways/genes | 
*AsyncIgvfCatalogApi* | [**pathways_from_pathways**](docs/AsyncIgvfCatalogApi.md#pathways_from_pathways) | **GET** /pathways/pathways | 
*AsyncIgvfCatalogApi* | [**annotations_from_go_terms**](docs/AsyncIgvfCatalogApi.md#annotations_from_go_terms) | **GET** /go-terms/gene-products | 
*AsyncIgvfCatalogApi* | [**go_terms_from_annotations**](docs/AsyncIgvfCatalogApi.md#go_terms_from_annotations) | **GET** /gene-products/go-terms | 
*AsyncIgvfCatalogApi* | [**variants_from_diseases**](docs/AsyncIgvfCatalogApi.md#variants_from_diseases) | **GET** /diseases/variants | 
*AsyncIgvfCatalogApi* | [**genes_from_diseases**](docs/AsyncIgvfCatalogApi.md#genes_from_diseases) | **GET** /diseases/genes | 
*AsyncIgvfCatalogApi* | [**variants_from_drugs**](docs/AsyncIgvfCatalogApi.md#variants_from_drugs) | **GET** /drugs/variants | 
*AsyncIgvfCatalogApi* | [**files_filesets**](docs/AsyncIgvfCatalogApi.md#files_filesets) | **GET** /files-filesets | 
*AsyncIgvfCatalogApi* | [**llm_query**](docs/AsyncIgvfCatalogApi.md#llm_query) | **POST** /llm-query | 
*AsyncIgvfCatalogApi* | [**genes_genomic_elements_score_summary**](docs/AsyncIgvfCatalogApi.md#genes_genomic_elements_score_summary) | **GET** /genes/genomic-elements/score-summary | 
*AsyncIgvfCatalogApi* | [**genes_transcripts_genomic_elements**](docs/AsyncIgvfCatalogApi.md#genes_transcripts_genomic_elements) | **GET** /genes/transcripts/genomic-elements | 
*AsyncIgvfCatalogApi* | [**genes_variants_score_summary**](docs/AsyncIgvfCatalogApi.md#genes_variants_score_summary) | **GET** /genes/variants/score-summary | 
*AsyncIgvfCatalogApi* | [**nearest_genes**](docs/AsyncIgvfCatalogApi.md#nearest_genes) | **GET** /nearest-genes | 

## Documentation For Models

 - [AccessibleGenomicElement](docs/AccessibleGenomicElement.md)
 - [AccessibleGenomicElement11](docs/AccessibleGenomicElement11.md)
 - [AccessibleGenomicElementPromoterOf](docs/AccessibleGenomicElementPromoterOf.md)
 - [Annotations](docs/Annotations.md)
 - [AnnotationsFromGoTerms](docs/AnnotationsFromGoTerms.md)
 - [Biosamples](docs/Biosamples.md)
 - [BiosamplesFromGenomicElements](docs/BiosamplesFromGenomicElements.md)
 - [BiosamplesFromGenomicElementsBiosample](docs/BiosamplesFromGenomicElementsBiosample.md)
 - [BiosamplesFromGenomicElementsGenomicElement](docs/BiosamplesFromGenomicElementsGenomicElement.md)
 - [BiosamplesFromVariants](docs/BiosamplesFromVariants.md)
 - [BiosamplesFromVariantsGenomicElement](docs/BiosamplesFromVariantsGenomicElement.md)
 - [BiosamplesFromVariantsVariant](docs/BiosamplesFromVariantsVariant.md)
 - [CaddScores](docs/CaddScores.md)
 - [CellTypes](docs/CellTypes.md)
 - [CellTypes2](docs/CellTypes2.md)
 - [CodingVariant](docs/CodingVariant.md)
 - [CodingVariants](docs/CodingVariants.md)
 - [CodingVariantsFromGenes](docs/CodingVariantsFromGenes.md)
 - [CodingVariantsFromPhenotypes](docs/CodingVariantsFromPhenotypes.md)
 - [CodingVariantsSummary](docs/CodingVariantsSummary.md)
 - [Complex](docs/Complex.md)
 - [ComplexComplexAssembly](docs/ComplexComplexAssembly.md)
 - [ComplexesFromProteins](docs/ComplexesFromProteins.md)
 - [ComplexesFromProteinsComplex](docs/ComplexesFromProteinsComplex.md)
 - [ComplexesFromProteinsProtein](docs/ComplexesFromProteinsProtein.md)
 - [DiseaseFromVariants](docs/DiseaseFromVariants.md)
 - [DiseaseFromVariantsSequenceVariant](docs/DiseaseFromVariantsSequenceVariant.md)
 - [DiseasesFromGenes](docs/DiseasesFromGenes.md)
 - [DiseasesFromGenesGene](docs/DiseasesFromGenesGene.md)
 - [Drug](docs/Drug.md)
 - [DrugsFromVariants](docs/DrugsFromVariants.md)
 - [DrugsFromVariantsDrug](docs/DrugsFromVariantsDrug.md)
 - [Elements](docs/Elements.md)
 - [EnhancerGenePredictions](docs/EnhancerGenePredictions.md)
 - [EnhancerGenePredictionsElements](docs/EnhancerGenePredictionsElements.md)
 - [FilesFilesets](docs/FilesFilesets.md)
 - [Gene](docs/Gene.md)
 - [Gene4](docs/Gene4.md)
 - [Gene6](docs/Gene6.md)
 - [GeneCompact](docs/GeneCompact.md)
 - [GeneNoSynonyms](docs/GeneNoSynonyms.md)
 - [GeneRef](docs/GeneRef.md)
 - [Genes](docs/Genes.md)
 - [Genes2](docs/Genes2.md)
 - [GenesFromGenomicElements](docs/GenesFromGenomicElements.md)
 - [GenesFromGenomicElementsGene](docs/GenesFromGenomicElementsGene.md)
 - [GenesFromGenomicElementsGenomicElement](docs/GenesFromGenomicElementsGenomicElement.md)
 - [GenesFromGenomicElementsPValue](docs/GenesFromGenomicElementsPValue.md)
 - [GenesFromPathways](docs/GenesFromPathways.md)
 - [GenesFromPathwaysPathway](docs/GenesFromPathwaysPathway.md)
 - [GenesFromProteins](docs/GenesFromProteins.md)
 - [GenesFromTranscripts](docs/GenesFromTranscripts.md)
 - [GenesFromTranscriptsTranscript](docs/GenesFromTranscriptsTranscript.md)
 - [GenesFromVariants](docs/GenesFromVariants.md)
 - [GenesFromVariantsSequenceVariant](docs/GenesFromVariantsSequenceVariant.md)
 - [GenesFromVariantsStudy](docs/GenesFromVariantsStudy.md)
 - [GenesGenes](docs/GenesGenes.md)
 - [GenesGenesGene1](docs/GenesGenesGene1.md)
 - [GenesGenomicElementsScoreSummary](docs/GenesGenomicElementsScoreSummary.md)
 - [GenesProteinsFromVariants](docs/GenesProteinsFromVariants.md)
 - [GenesProteinsGenesProteins](docs/GenesProteinsGenesProteins.md)
 - [GenesStructure](docs/GenesStructure.md)
 - [GenesTranscriptsGenes](docs/GenesTranscriptsGenes.md)
 - [GenesTranscriptsGenesTranscript](docs/GenesTranscriptsGenesTranscript.md)
 - [GenesTranscriptsGenomicElements](docs/GenesTranscriptsGenomicElements.md)
 - [GenesTranscriptsGenomicElementsAccessibleGenomicElement](docs/GenesTranscriptsGenomicElementsAccessibleGenomicElement.md)
 - [GenesVariantsScoreSummary](docs/GenesVariantsScoreSummary.md)
 - [GenomicElement](docs/GenomicElement.md)
 - [GenomicElement2](docs/GenomicElement2.md)
 - [GenomicElement4](docs/GenomicElement4.md)
 - [GenomicElement5](docs/GenomicElement5.md)
 - [GenomicElement7](docs/GenomicElement7.md)
 - [GenomicElement9](docs/GenomicElement9.md)
 - [GenomicElementFull](docs/GenomicElementFull.md)
 - [GenomicElementsFromGenomicElements](docs/GenomicElementsFromGenomicElements.md)
 - [GenomicElementsFromGenomicElementsPerturbedGenomicElement](docs/GenomicElementsFromGenomicElementsPerturbedGenomicElement.md)
 - [GenomicElementsFromPhenotypes](docs/GenomicElementsFromPhenotypes.md)
 - [GenomicElementsFromPhenotypesPhenotype](docs/GenomicElementsFromPhenotypesPhenotype.md)
 - [GenomicElementsFromVariants](docs/GenomicElementsFromVariants.md)
 - [GenomicElementsPredictionsFromVariant](docs/GenomicElementsPredictionsFromVariant.md)
 - [Grn](docs/Grn.md)
 - [Groups](docs/Groups.md)
 - [Groups13](docs/Groups13.md)
 - [IdName](docs/IdName.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObjectIssuesInner](docs/InlineObjectIssuesInner.md)
 - [LinkedFeature](docs/LinkedFeature.md)
 - [LlmQuery](docs/LlmQuery.md)
 - [LlmQueryRequest](docs/LlmQueryRequest.md)
 - [MethodCount](docs/MethodCount.md)
 - [MethodsAndContexts](docs/MethodsAndContexts.md)
 - [Motif](docs/Motif.md)
 - [MotifsFromProteins](docs/MotifsFromProteins.md)
 - [MotifsFromProteinsMotif](docs/MotifsFromProteinsMotif.md)
 - [NearestGene](docs/NearestGene.md)
 - [NearestGenes](docs/NearestGenes.md)
 - [OntologyTerm](docs/OntologyTerm.md)
 - [OntologyTermBasic](docs/OntologyTermBasic.md)
 - [OntologyTermChildren](docs/OntologyTermChildren.md)
 - [OntologyTermTransitiveClosure](docs/OntologyTermTransitiveClosure.md)
 - [Paths](docs/Paths.md)
 - [Pathway](docs/Pathway.md)
 - [PathwaysFromPathways](docs/PathwaysFromPathways.md)
 - [Phenotype](docs/Phenotype.md)
 - [PhenotypeRef](docs/PhenotypeRef.md)
 - [PhenotypesFromVariants](docs/PhenotypesFromVariants.md)
 - [PhenotypesFromVariants37](docs/PhenotypesFromVariants37.md)
 - [PhenotypesFromVariantsStudy](docs/PhenotypesFromVariantsStudy.md)
 - [PhenotypesFromVariantsVariant](docs/PhenotypesFromVariantsVariant.md)
 - [Predictions](docs/Predictions.md)
 - [Predictions2](docs/Predictions2.md)
 - [PredictionsFromVariants](docs/PredictionsFromVariants.md)
 - [PropertyScores](docs/PropertyScores.md)
 - [Protein](docs/Protein.md)
 - [ProteinBasic](docs/ProteinBasic.md)
 - [ProteinChange](docs/ProteinChange.md)
 - [ProteinCompact](docs/ProteinCompact.md)
 - [ProteinComplexOption](docs/ProteinComplexOption.md)
 - [ProteinsFromTranscripts](docs/ProteinsFromTranscripts.md)
 - [ProteinsFromTranscriptsProtein](docs/ProteinsFromTranscriptsProtein.md)
 - [ProteinsFromVariants](docs/ProteinsFromVariants.md)
 - [ProteinsFromVariantsBiosampleTerm](docs/ProteinsFromVariantsBiosampleTerm.md)
 - [ProteinsFromVariantsProteinComplex](docs/ProteinsFromVariantsProteinComplex.md)
 - [ProteinsProteins](docs/ProteinsProteins.md)
 - [ProteinsProteinsProtein1](docs/ProteinsProteinsProtein1.md)
 - [QtlSummaryEndpoint](docs/QtlSummaryEndpoint.md)
 - [Qtls](docs/Qtls.md)
 - [Qtls3](docs/Qtls3.md)
 - [Related](docs/Related.md)
 - [RelatedGene](docs/RelatedGene.md)
 - [RelatedItem](docs/RelatedItem.md)
 - [RelatedSources](docs/RelatedSources.md)
 - [Scores](docs/Scores.md)
 - [SequenceVariant](docs/SequenceVariant.md)
 - [SequenceVariant9](docs/SequenceVariant9.md)
 - [Sources](docs/Sources.md)
 - [Sources4](docs/Sources4.md)
 - [Study](docs/Study.md)
 - [Study2](docs/Study2.md)
 - [StudyParameters](docs/StudyParameters.md)
 - [Summary](docs/Summary.md)
 - [TargetGene](docs/TargetGene.md)
 - [TfBinding](docs/TfBinding.md)
 - [Transcript](docs/Transcript.md)
 - [Variant](docs/Variant.md)
 - [VariantAnnotations](docs/VariantAnnotations.md)
 - [VariantBasic](docs/VariantBasic.md)
 - [VariantMinimal](docs/VariantMinimal.md)
 - [VariantRef](docs/VariantRef.md)
 - [VariantSummary](docs/VariantSummary.md)
 - [Variants](docs/Variants.md)
 - [VariantsAllelesValue](docs/VariantsAllelesValue.md)
 - [VariantsFromDrugs](docs/VariantsFromDrugs.md)
 - [VariantsFromPhenotypesItem](docs/VariantsFromPhenotypesItem.md)
 - [VariantsFromVariantID](docs/VariantsFromVariantID.md)
 - [VariantsFromVariantIDSequenceVariant](docs/VariantsFromVariantIDSequenceVariant.md)
 - [VariantsFromVariantIDSummary](docs/VariantsFromVariantIDSummary.md)
 - [VariantsGenomicElementsGenes](docs/VariantsGenomicElementsGenes.md)
 - [VariantsRegionSummary](docs/VariantsRegionSummary.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: Bearer authentication


## Author

encode-help@lists.stanford.edu


