"""Offline checks that the generated client imports and exposes the API."""

import asyncio
from importlib.metadata import version

import igvf_catalog_async_client


def test_version_matches_metadata():
    assert igvf_catalog_async_client.__version__ == version("igvf_catalog_async_client")


def test_api_methods():
    async def check():
        async with igvf_catalog_async_client.ApiClient() as api_client:
            api = igvf_catalog_async_client.AsyncIgvfCatalogApi(api_client)
            for name in ["genes", "variants", "genes_from_variants", "llm_query"]:
                assert asyncio.iscoroutinefunction(getattr(api, name))

    asyncio.run(check())


def test_configuration_host():
    configuration = igvf_catalog_async_client.Configuration(host="https://example.org/api")
    assert configuration.host == "https://example.org/api"
