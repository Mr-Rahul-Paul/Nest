
# OWASP API v0

## Important points

When working on this API, **always follow these rules** to avoid breaking clients:

- The authentication class in `__init__.py` **must be named `ApiKey`**.
  - The client’s `api_key` parameter is automatically derived from this name.
  - **Do not rename this class**, only update its implementation if needed.

- Each API endpoint must have a **unique `operationId`** in the OpenAPI specification.
  - Duplicate `operationId`s will break client SDK generation and cause method conflicts.

- Endpoint naming documentation:
  - [Customize methods](https://www.speakeasy.com/docs/customize/methods)
  - [Customize namespaces](https://www.speakeasy.com/docs/customize/structure/namespaces)

## Versioning

The OWASP Nest REST API uses **date-based versioning** (e.g., `2026-03-03`).

- **Stable Paths:** The URL path prefix (e.g., `/api/v0/`) remains stable. Backward compatibility is maintained for existing prefixes.
- **SDK Packaging:** Generated SDKs are versioned using the date of the release (e.g., `v2026.03.03` for NPM packages).
- **Choosing an SDK:** Consumers should select the SDK package version corresponding to the release date of the API they intend to target, or use the newest available if targeting the latest deployment.
