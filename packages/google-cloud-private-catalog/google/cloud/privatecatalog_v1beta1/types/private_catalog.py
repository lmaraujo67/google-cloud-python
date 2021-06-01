# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import proto  # type: ignore

from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.privatecatalog.v1beta1",
    manifest={
        "SearchCatalogsRequest",
        "SearchCatalogsResponse",
        "SearchProductsRequest",
        "SearchProductsResponse",
        "SearchVersionsRequest",
        "SearchVersionsResponse",
        "Catalog",
        "Product",
        "AssetReference",
        "Inputs",
        "GcsSource",
        "GitSource",
        "Version",
    },
)


class SearchCatalogsRequest(proto.Message):
    r"""Request message for
    [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].

    Attributes:
        resource (str):
            Required. The name of the resource context. It can be in
            following formats:

            -  ``projects/{project}``
            -  ``folders/{folder}``
            -  ``organizations/{organization}``
        query (str):
            The query to filter the catalogs. The supported queries are:

            -  Get a single catalog: ``name=catalogs/{catalog}``
        page_size (int):
            The maximum number of entries that are
            requested.
        page_token (str):
            A pagination token returned from a previous
            call to SearchCatalogs that indicates where this
            listing should continue from.
    """

    resource = proto.Field(proto.STRING, number=1,)
    query = proto.Field(proto.STRING, number=2,)
    page_size = proto.Field(proto.INT32, number=3,)
    page_token = proto.Field(proto.STRING, number=4,)


class SearchCatalogsResponse(proto.Message):
    r"""Response message for
    [PrivateCatalog.SearchCatalogs][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchCatalogs].

    Attributes:
        catalogs (Sequence[google.cloud.privatecatalog_v1beta1.types.Catalog]):
            The ``Catalog``\ s computed from the resource context.
        next_page_token (str):
            A pagination token returned from a previous
            call to SearchCatalogs that indicates from where
            listing should continue.
    """

    @property
    def raw_page(self):
        return self

    catalogs = proto.RepeatedField(proto.MESSAGE, number=1, message="Catalog",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class SearchProductsRequest(proto.Message):
    r"""Request message for
    [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

    Attributes:
        resource (str):
            Required. The name of the resource context. See
            [SearchCatalogsRequest.resource][google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest.resource]
            for details.
        query (str):
            The query to filter the products.

            The supported queries are:

            -  List products of all catalogs: empty
            -  List products under a catalog:
               ``parent=catalogs/{catalog}``
            -  Get a product by name:
               ``name=catalogs/{catalog}/products/{product}``
        page_size (int):
            The maximum number of entries that are
            requested.
        page_token (str):
            A pagination token returned from a previous
            call to SearchProducts that indicates where this
            listing should continue from.
    """

    resource = proto.Field(proto.STRING, number=1,)
    query = proto.Field(proto.STRING, number=2,)
    page_size = proto.Field(proto.INT32, number=3,)
    page_token = proto.Field(proto.STRING, number=4,)


class SearchProductsResponse(proto.Message):
    r"""Response message for
    [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

    Attributes:
        products (Sequence[google.cloud.privatecatalog_v1beta1.types.Product]):
            The ``Product`` resources computed from the resource
            context.
        next_page_token (str):
            A pagination token returned from a previous
            call to SearchProducts that indicates from where
            listing should continue.
    """

    @property
    def raw_page(self):
        return self

    products = proto.RepeatedField(proto.MESSAGE, number=1, message="Product",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class SearchVersionsRequest(proto.Message):
    r"""Request message for
    [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].

    Attributes:
        resource (str):
            Required. The name of the resource context. See
            [SearchCatalogsRequest.resource][google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest.resource]
            for details.
        query (str):
            Required. The query to filter the versions.

            The supported queries are:

            -  List versions under a product:
               ``parent=catalogs/{catalog}/products/{product}``
            -  Get a version by name:
               ``name=catalogs/{catalog}/products/{product}/versions/{version}``
        page_size (int):
            The maximum number of entries that are
            requested.
        page_token (str):
            A pagination token returned from a previous
            call to SearchVersions that indicates where this
            listing should continue from.
    """

    resource = proto.Field(proto.STRING, number=1,)
    query = proto.Field(proto.STRING, number=2,)
    page_size = proto.Field(proto.INT32, number=3,)
    page_token = proto.Field(proto.STRING, number=4,)


class SearchVersionsResponse(proto.Message):
    r"""Response message for
    [PrivateCatalog.SearchVersions][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchVersions].

    Attributes:
        versions (Sequence[google.cloud.privatecatalog_v1beta1.types.Version]):
            The ``Version`` resources computed from the resource
            context.
        next_page_token (str):
            A pagination token returned from a previous
            call to SearchVersions that indicates from where
            the listing should continue.
    """

    @property
    def raw_page(self):
        return self

    versions = proto.RepeatedField(proto.MESSAGE, number=1, message="Version",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class Catalog(proto.Message):
    r"""The readonly representation of a catalog computed with a
    given resource context.

    Attributes:
        name (str):
            Output only. The resource name of the target catalog, in the
            format of \`catalogs/{catalog}'.
        display_name (str):
            Output only. The descriptive name of the
            catalog as it appears in UIs.
        description (str):
            Output only. The description of the catalog.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the catalog was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the catalog was
            last updated.
    """

    name = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    description = proto.Field(proto.STRING, number=3,)
    create_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=5, message=timestamp_pb2.Timestamp,)


class Product(proto.Message):
    r"""The readonly representation of a product computed with a
    given resource context.

    Attributes:
        name (str):
            Output only. The resource name of the target product, in the
            format of \`products/[a-z][-a-z0-9]*[a-z0-9]'.

            A unique identifier for the product under a catalog.
        asset_type (str):
            Output only. The type of the product asset. It can be one of
            the following values:

            -  ``google.deploymentmanager.Template``
            -  ``google.cloudprivatecatalog.ListingOnly``
            -  ``google.cloudprivatecatalog.Terraform``
        display_metadata (google.protobuf.struct_pb2.Struct):
            Required. Output only. The display metadata to describe the
            product. The JSON schema of the metadata differs by
            [Product.asset_type][google.cloud.privatecatalog.v1beta1.Product.asset_type].
            When the type is ``google.deploymentmanager.Template``, the
            schema is as follows:

            ::

               "$schema": http://json-schema.org/draft-04/schema#
               type: object
               properties:
                 name:
                   type: string
                   minLength: 1
                   maxLength: 64
                 description:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 tagline:
                   type: string
                   minLength: 1
                   maxLength: 100
                 support_info:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 creator:
                   type: string
                   minLength: 1
                   maxLength: 100
                 documentations:
                   type: array
                   items:
                     type: object
                     properties:
                       url:
                         type: string
                         pattern:
                         "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                       title:
                         type: string
                         minLength: 1
                         maxLength: 64
                       description:
                         type: string
                         minLength: 1
                         maxLength: 2048
               required:
               - name
               - description
               additionalProperties: false

            When the asset type is
            ``google.cloudprivatecatalog.ListingOnly``, the schema is as
            follows:

            ::

               "$schema": http://json-schema.org/draft-04/schema#
               type: object
               properties:
                 name:
                   type: string
                   minLength: 1
                   maxLength: 64
                 description:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 tagline:
                   type: string
                   minLength: 1
                   maxLength: 100
                 support_info:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 creator:
                   type: string
                   minLength: 1
                   maxLength: 100
                 documentations:
                   type: array
                   items:
                     type: object
                     properties:
                       url:
                         type: string
                         pattern:
                         "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                       title:
                         type: string
                         minLength: 1
                         maxLength: 64
                       description:
                         type: string
                         minLength: 1
                         maxLength: 2048
                 signup_url:
                   type: string
                   pattern:
                   "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
               required:
               - name
               - description
               - signup_url
               additionalProperties: false

            When the asset type is
            ``google.cloudprivatecatalog.Terraform``, the schema is as
            follows:

            ::

               "$schema": http://json-schema.org/draft-04/schema#
               type: object
               properties:
                 name:
                   type: string
                   minLength: 1
                   maxLength: 64
                 description:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 tagline:
                   type: string
                   minLength: 1
                   maxLength: 100
                 support_info:
                   type: string
                   minLength: 1
                   maxLength: 2048
                 creator:
                   type: string
                   minLength: 1
                   maxLength: 100
                 documentations:
                   type: array
                   items:
                     type: object
                     properties:
                       url:
                         type: string
                         pattern:
                         "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"
                       title:
                         type: string
                         minLength: 1
                         maxLength: 64
                       description:
                         type: string
                         minLength: 1
                         maxLength: 2048
               required:
               - name
               - description
               additionalProperties: true
        icon_uri (str):
            Output only. The icon URI of the product.
        asset_references (Sequence[google.cloud.privatecatalog_v1beta1.types.AssetReference]):
            Output only. A collection of assets referred
            by a product. This field is set for Terraform
            Products only.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the product was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the product was
            last updated.
    """

    name = proto.Field(proto.STRING, number=1,)
    asset_type = proto.Field(proto.STRING, number=2,)
    display_metadata = proto.Field(proto.MESSAGE, number=3, message=struct_pb2.Struct,)
    icon_uri = proto.Field(proto.STRING, number=4,)
    asset_references = proto.RepeatedField(
        proto.MESSAGE, number=10, message="AssetReference",
    )
    create_time = proto.Field(proto.MESSAGE, number=5, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=6, message=timestamp_pb2.Timestamp,)


class AssetReference(proto.Message):
    r"""Defines the reference of an asset belonging to a product.
    Attributes:
        id (str):
            Output only. A unique identifier among asset
            references in a product.
        description (str):
            Output only. The human-readable description
            of the referenced asset. Maximum 256 characters
            in length.
        inputs (google.cloud.privatecatalog_v1beta1.types.Inputs):
            Output only. The definition of input
            parameters to hydrate the asset template.
        validation_status (google.cloud.privatecatalog_v1beta1.types.AssetReference.AssetValidationState):
            Output only. The current state of the asset
            reference.
        validation_operation (google.longrunning.operations_pb2.Operation):
            Output only. The validation process metadata.
        asset (str):
            Output only. The asset resource name if an
            asset is hosted by Private Catalog.
        gcs_path (str):
            Output only. The cloud storage object path.
        git_source (google.cloud.privatecatalog_v1beta1.types.GitSource):
            Output only. The git source.
        gcs_source (google.cloud.privatecatalog_v1beta1.types.GcsSource):
            Output only. The cloud storage source.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of the
            asset reference.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of the
            asset reference.
        version (str):
            The version of the source used for this asset
            reference.
    """

    class AssetValidationState(proto.Enum):
        r"""Possible validation steates of an asset reference."""
        ASSET_VALIDATION_STATE_UNSPECIFIED = 0
        PENDING = 1
        VALID = 2
        INVALID = 3

    id = proto.Field(proto.STRING, number=1,)
    description = proto.Field(proto.STRING, number=2,)
    inputs = proto.Field(proto.MESSAGE, number=6, message="Inputs",)
    validation_status = proto.Field(proto.ENUM, number=7, enum=AssetValidationState,)
    validation_operation = proto.Field(
        proto.MESSAGE, number=8, message=operations_pb2.Operation,
    )
    asset = proto.Field(proto.STRING, number=10, oneof="source",)
    gcs_path = proto.Field(proto.STRING, number=11, oneof="source",)
    git_source = proto.Field(
        proto.MESSAGE, number=15, oneof="source", message="GitSource",
    )
    gcs_source = proto.Field(proto.MESSAGE, number=16, message="GcsSource",)
    create_time = proto.Field(
        proto.MESSAGE, number=12, message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE, number=13, message=timestamp_pb2.Timestamp,
    )
    version = proto.Field(proto.STRING, number=14,)


class Inputs(proto.Message):
    r"""Defines definition of input parameters of asset templates.
    Attributes:
        parameters (google.protobuf.struct_pb2.Struct):
            Output only. The JSON schema defining the
            inputs and their formats.
    """

    parameters = proto.Field(proto.MESSAGE, number=1, message=struct_pb2.Struct,)


class GcsSource(proto.Message):
    r"""Defines how to access Cloud Storage source.
    Attributes:
        gcs_path (str):
            Output only. the cloud storage object path.
        generation (int):
            Output only. Generation of the object, which
            is set when the content of an object starts
            being written.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the object
            metadata was last changed.
    """

    gcs_path = proto.Field(proto.STRING, number=1,)
    generation = proto.Field(proto.INT64, number=2,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)


class GitSource(proto.Message):
    r"""Defines how to access a Git Source.
    Attributes:
        repo (str):
            Location of the Git repo to build.
        dir_ (str):
            Directory, relative to the source root, in which to run the
            build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution.
        commit (str):
            The revision commit to use.
        branch (str):
            The revision branch to use.
        tag (str):
            The revision tag to use.
    """

    repo = proto.Field(proto.STRING, number=1,)
    dir_ = proto.Field(proto.STRING, number=2,)
    commit = proto.Field(proto.STRING, number=3, oneof="ref",)
    branch = proto.Field(proto.STRING, number=4, oneof="ref",)
    tag = proto.Field(proto.STRING, number=5, oneof="ref",)


class Version(proto.Message):
    r"""The consumer representation of a version which is a child resource
    under a ``Product`` with asset data.

    Attributes:
        name (str):
            Output only. The resource name of the version, in the format
            \`catalogs/{catalog}/products/{product}/versions/[a-z][-a-z0-9]*[a-z0-9]'.

            A unique identifier for the version under a product.
        description (str):
            Output only. The user-supplied description of
            the version. Maximum of 256 characters.
        asset (google.protobuf.struct_pb2.Struct):
            Output only. The asset which has been validated and is ready
            to be provisioned. See
            [google.cloud.privatecatalogproducer.v1beta.Version.asset][]
            for details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the version was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the version was
            last updated.
    """

    name = proto.Field(proto.STRING, number=1,)
    description = proto.Field(proto.STRING, number=2,)
    asset = proto.Field(proto.MESSAGE, number=3, message=struct_pb2.Struct,)
    create_time = proto.Field(proto.MESSAGE, number=5, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=6, message=timestamp_pb2.Timestamp,)


__all__ = tuple(sorted(__protobuf__.manifest))
