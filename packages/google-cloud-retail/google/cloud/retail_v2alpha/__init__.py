# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.retail_v2alpha import gapic_version as package_version

__version__ = package_version.__version__


from .services.catalog_service import CatalogServiceAsyncClient, CatalogServiceClient
from .services.completion_service import (
    CompletionServiceAsyncClient,
    CompletionServiceClient,
)
from .services.control_service import ControlServiceAsyncClient, ControlServiceClient
from .services.merchant_center_account_link_service import (
    MerchantCenterAccountLinkServiceAsyncClient,
    MerchantCenterAccountLinkServiceClient,
)
from .services.model_service import ModelServiceAsyncClient, ModelServiceClient
from .services.prediction_service import (
    PredictionServiceAsyncClient,
    PredictionServiceClient,
)
from .services.product_service import ProductServiceAsyncClient, ProductServiceClient
from .services.search_service import SearchServiceAsyncClient, SearchServiceClient
from .services.serving_config_service import (
    ServingConfigServiceAsyncClient,
    ServingConfigServiceClient,
)
from .services.user_event_service import (
    UserEventServiceAsyncClient,
    UserEventServiceClient,
)
from .types.catalog import (
    AttributesConfig,
    Catalog,
    CatalogAttribute,
    CompletionConfig,
    MerchantCenterFeedFilter,
    MerchantCenterLink,
    MerchantCenterLinkingConfig,
    ProductLevelConfig,
)
from .types.catalog_service import (
    AddCatalogAttributeRequest,
    BatchRemoveCatalogAttributesRequest,
    BatchRemoveCatalogAttributesResponse,
    GetAttributesConfigRequest,
    GetCompletionConfigRequest,
    GetDefaultBranchRequest,
    GetDefaultBranchResponse,
    ListCatalogsRequest,
    ListCatalogsResponse,
    RemoveCatalogAttributeRequest,
    ReplaceCatalogAttributeRequest,
    SetDefaultBranchRequest,
    UpdateAttributesConfigRequest,
    UpdateCatalogRequest,
    UpdateCompletionConfigRequest,
)
from .types.common import (
    AttributeConfigLevel,
    Audience,
    ColorInfo,
    Condition,
    CustomAttribute,
    FulfillmentInfo,
    Image,
    Interval,
    LocalInventory,
    PriceInfo,
    Rating,
    RecommendationsFilteringOption,
    Rule,
    SearchSolutionUseCase,
    SolutionType,
    UserInfo,
)
from .types.completion_service import CompleteQueryRequest, CompleteQueryResponse
from .types.control import Control
from .types.control_service import (
    CreateControlRequest,
    DeleteControlRequest,
    GetControlRequest,
    ListControlsRequest,
    ListControlsResponse,
    UpdateControlRequest,
)
from .types.export_config import (
    BigQueryOutputResult,
    ExportErrorsConfig,
    ExportMetadata,
    ExportProductsResponse,
    ExportUserEventsResponse,
    GcsOutputResult,
    OutputResult,
)
from .types.import_config import (
    BigQuerySource,
    CompletionDataInputConfig,
    GcsSource,
    ImportCompletionDataRequest,
    ImportCompletionDataResponse,
    ImportErrorsConfig,
    ImportMetadata,
    ImportProductsRequest,
    ImportProductsResponse,
    ImportUserEventsRequest,
    ImportUserEventsResponse,
    ProductInlineSource,
    ProductInputConfig,
    TransformedUserEventsMetadata,
    UserEventImportSummary,
    UserEventInlineSource,
    UserEventInputConfig,
)
from .types.merchant_center_account_link import (
    CreateMerchantCenterAccountLinkMetadata,
    MerchantCenterAccountLink,
)
from .types.merchant_center_account_link_service import (
    CreateMerchantCenterAccountLinkRequest,
    DeleteMerchantCenterAccountLinkRequest,
    ListMerchantCenterAccountLinksRequest,
    ListMerchantCenterAccountLinksResponse,
)
from .types.model import Model
from .types.model_service import (
    CreateModelMetadata,
    CreateModelRequest,
    DeleteModelRequest,
    GetModelRequest,
    ListModelsRequest,
    ListModelsResponse,
    PauseModelRequest,
    ResumeModelRequest,
    TuneModelMetadata,
    TuneModelRequest,
    TuneModelResponse,
    UpdateModelRequest,
)
from .types.prediction_service import PredictRequest, PredictResponse
from .types.product import Product
from .types.product_service import (
    AddFulfillmentPlacesMetadata,
    AddFulfillmentPlacesRequest,
    AddFulfillmentPlacesResponse,
    AddLocalInventoriesMetadata,
    AddLocalInventoriesRequest,
    AddLocalInventoriesResponse,
    CreateProductRequest,
    DeleteProductRequest,
    GetProductRequest,
    ListProductsRequest,
    ListProductsResponse,
    RemoveFulfillmentPlacesMetadata,
    RemoveFulfillmentPlacesRequest,
    RemoveFulfillmentPlacesResponse,
    RemoveLocalInventoriesMetadata,
    RemoveLocalInventoriesRequest,
    RemoveLocalInventoriesResponse,
    SetInventoryMetadata,
    SetInventoryRequest,
    SetInventoryResponse,
    UpdateProductRequest,
)
from .types.promotion import Promotion
from .types.purge_config import (
    PurgeMetadata,
    PurgeProductsMetadata,
    PurgeProductsRequest,
    PurgeProductsResponse,
    PurgeUserEventsRequest,
    PurgeUserEventsResponse,
)
from .types.search_service import ExperimentInfo, SearchRequest, SearchResponse
from .types.serving_config import ServingConfig
from .types.serving_config_service import (
    AddControlRequest,
    CreateServingConfigRequest,
    DeleteServingConfigRequest,
    GetServingConfigRequest,
    ListServingConfigsRequest,
    ListServingConfigsResponse,
    RemoveControlRequest,
    UpdateServingConfigRequest,
)
from .types.user_event import (
    CompletionDetail,
    ProductDetail,
    PurchaseTransaction,
    UserEvent,
)
from .types.user_event_service import (
    CollectUserEventRequest,
    RejoinUserEventsMetadata,
    RejoinUserEventsRequest,
    RejoinUserEventsResponse,
    WriteUserEventRequest,
)

__all__ = (
    "CatalogServiceAsyncClient",
    "CompletionServiceAsyncClient",
    "ControlServiceAsyncClient",
    "MerchantCenterAccountLinkServiceAsyncClient",
    "ModelServiceAsyncClient",
    "PredictionServiceAsyncClient",
    "ProductServiceAsyncClient",
    "SearchServiceAsyncClient",
    "ServingConfigServiceAsyncClient",
    "UserEventServiceAsyncClient",
    "AddCatalogAttributeRequest",
    "AddControlRequest",
    "AddFulfillmentPlacesMetadata",
    "AddFulfillmentPlacesRequest",
    "AddFulfillmentPlacesResponse",
    "AddLocalInventoriesMetadata",
    "AddLocalInventoriesRequest",
    "AddLocalInventoriesResponse",
    "AttributeConfigLevel",
    "AttributesConfig",
    "Audience",
    "BatchRemoveCatalogAttributesRequest",
    "BatchRemoveCatalogAttributesResponse",
    "BigQueryOutputResult",
    "BigQuerySource",
    "Catalog",
    "CatalogAttribute",
    "CatalogServiceClient",
    "CollectUserEventRequest",
    "ColorInfo",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "CompletionConfig",
    "CompletionDataInputConfig",
    "CompletionDetail",
    "CompletionServiceClient",
    "Condition",
    "Control",
    "ControlServiceClient",
    "CreateControlRequest",
    "CreateMerchantCenterAccountLinkMetadata",
    "CreateMerchantCenterAccountLinkRequest",
    "CreateModelMetadata",
    "CreateModelRequest",
    "CreateProductRequest",
    "CreateServingConfigRequest",
    "CustomAttribute",
    "DeleteControlRequest",
    "DeleteMerchantCenterAccountLinkRequest",
    "DeleteModelRequest",
    "DeleteProductRequest",
    "DeleteServingConfigRequest",
    "ExperimentInfo",
    "ExportErrorsConfig",
    "ExportMetadata",
    "ExportProductsResponse",
    "ExportUserEventsResponse",
    "FulfillmentInfo",
    "GcsOutputResult",
    "GcsSource",
    "GetAttributesConfigRequest",
    "GetCompletionConfigRequest",
    "GetControlRequest",
    "GetDefaultBranchRequest",
    "GetDefaultBranchResponse",
    "GetModelRequest",
    "GetProductRequest",
    "GetServingConfigRequest",
    "Image",
    "ImportCompletionDataRequest",
    "ImportCompletionDataResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportProductsRequest",
    "ImportProductsResponse",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "Interval",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "ListControlsRequest",
    "ListControlsResponse",
    "ListMerchantCenterAccountLinksRequest",
    "ListMerchantCenterAccountLinksResponse",
    "ListModelsRequest",
    "ListModelsResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "ListServingConfigsRequest",
    "ListServingConfigsResponse",
    "LocalInventory",
    "MerchantCenterAccountLink",
    "MerchantCenterAccountLinkServiceClient",
    "MerchantCenterFeedFilter",
    "MerchantCenterLink",
    "MerchantCenterLinkingConfig",
    "Model",
    "ModelServiceClient",
    "OutputResult",
    "PauseModelRequest",
    "PredictRequest",
    "PredictResponse",
    "PredictionServiceClient",
    "PriceInfo",
    "Product",
    "ProductDetail",
    "ProductInlineSource",
    "ProductInputConfig",
    "ProductLevelConfig",
    "ProductServiceClient",
    "Promotion",
    "PurchaseTransaction",
    "PurgeMetadata",
    "PurgeProductsMetadata",
    "PurgeProductsRequest",
    "PurgeProductsResponse",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "Rating",
    "RecommendationsFilteringOption",
    "RejoinUserEventsMetadata",
    "RejoinUserEventsRequest",
    "RejoinUserEventsResponse",
    "RemoveCatalogAttributeRequest",
    "RemoveControlRequest",
    "RemoveFulfillmentPlacesMetadata",
    "RemoveFulfillmentPlacesRequest",
    "RemoveFulfillmentPlacesResponse",
    "RemoveLocalInventoriesMetadata",
    "RemoveLocalInventoriesRequest",
    "RemoveLocalInventoriesResponse",
    "ReplaceCatalogAttributeRequest",
    "ResumeModelRequest",
    "Rule",
    "SearchRequest",
    "SearchResponse",
    "SearchServiceClient",
    "SearchSolutionUseCase",
    "ServingConfig",
    "ServingConfigServiceClient",
    "SetDefaultBranchRequest",
    "SetInventoryMetadata",
    "SetInventoryRequest",
    "SetInventoryResponse",
    "SolutionType",
    "TransformedUserEventsMetadata",
    "TuneModelMetadata",
    "TuneModelRequest",
    "TuneModelResponse",
    "UpdateAttributesConfigRequest",
    "UpdateCatalogRequest",
    "UpdateCompletionConfigRequest",
    "UpdateControlRequest",
    "UpdateModelRequest",
    "UpdateProductRequest",
    "UpdateServingConfigRequest",
    "UserEvent",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventInputConfig",
    "UserEventServiceClient",
    "UserInfo",
    "WriteUserEventRequest",
)
