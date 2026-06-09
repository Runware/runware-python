"""Types for the content namespace.

These mirror the public response shapes from the Runware content service —
metadata about curated models, creators, collections, capabilities, pricing.

Convention: ``creator``, ``capabilities``, ``architecture``, ``basedOn`` are
ids (strings). Resolve them client-side against the appropriate listing
method. The exception is ``/collections`` and ``/creators``, whose ``models``
field is resolved server-side to full ``ModelMetadata`` objects (one level
only — the inner models' own ids stay as strings).
"""

from __future__ import annotations

from typing import Any, Generic, Literal, TypedDict, TypeVar


class PricingExample(TypedDict, total=False):
    configuration: str
    price: str
    competitorPrice: str


class ModelMetadata(TypedDict, total=False):
    model: str
    air: str
    name: str
    creator: str
    capabilities: list[str]
    architecture: str
    hosted: bool
    status: str
    releasedAt: str
    weight: float
    headline: str
    description: str
    coverImage: str
    ogImage: str
    pricingOverview: str
    pricingExamples: list[PricingExample]


class ArchitectureMetadata(TypedDict, total=False):
    id: str
    name: str
    status: str
    creator: str
    capabilities: list[str]
    basedOn: str
    releasedAt: str
    headline: str
    description: str
    coverImage: str
    ogImage: str


class Creator(TypedDict, total=False):
    id: str
    name: str
    logo: str
    headline: str
    description: str


class Capability(TypedDict):
    id: str
    label: str


class CollectionMetadata(TypedDict, total=False):
    id: str
    name: str
    order: float
    headline: str
    description: str
    icon: str
    coverImage: str
    category: list[str]
    models: list[str]


class CollectionWithModels(TypedDict, total=False):
    id: str
    name: str
    order: float
    headline: str
    description: str
    icon: str
    coverImage: str
    category: list[str]
    models: list[ModelMetadata]


class CreatorWithModels(TypedDict, total=False):
    id: str
    name: str
    logo: str
    headline: str
    description: str
    models: list[ModelMetadata]


class ExampleMetadata(TypedDict, total=False):
    id: str
    title: str
    model: str
    capability: str
    asset: str | None
    # Example request/response shapes vary per model — accept any payload.
    request: dict[str, Any]  # pyright: ignore[reportExplicitAny]
    response: dict[str, Any]  # pyright: ignore[reportExplicitAny]


class PricingModelListItem(TypedDict, total=False):
    model: str
    air: str
    name: str
    status: str
    coverImage: str
    releasedAt: str
    pricingOverview: str
    pricingExamples: list[PricingExample]
    category: list[str]


class GuideMetadata(TypedDict, total=False):
    slug: str
    title: str
    description: str
    date: str
    url: str


T = TypeVar("T")


class PaginatedResponse(TypedDict, Generic[T]):
    total: int
    limit: int
    offset: int
    items: list[T]


SortKey = Literal[
    "weight",
    "releasedAt",
    "name",
    "creator",
    "popularity",
    "newest",
    "alpha",
]
SortOrder = Literal["asc", "desc"]
Category = Literal["image", "video", "audio", "text", "3d"]


class ListModelsOptions(TypedDict, total=False):
    capability: str
    status: str
    category: Category
    creator: str
    search: str
    sort: SortKey
    order: SortOrder
    paginate: bool
    limit: int
    offset: int


class ListCollectionsOptions(TypedDict, total=False):
    category: str


class GetModelExamplesOptions(TypedDict, total=False):
    capability: str
