# Migration .NET 8

La fin du support de .NET 6 est prévue pour le [12 novembre 2024](https://dotnet.microsoft.com/en-us/platform/support/policy#dotnet-core). La migration vers la version .NET 8 doit dés lors être entreprise.

Cette documentation participative regroupe les informations récolter au sujet de .NET 8 et des problématiques de migrations.

- **[Breaking Change](./breaking-change/breaking-change.md)** : la liste non exhaustive des breaking changes .NET 7 et .NET 8 avec une idée des implications éventuelles.
- **[Performance](./performance/performance.md)** : la présentation des points d'améliorations des performances.

## Work in progress

- Breaking Change
    - [.NET 8](https://learn.microsoft.com/en-us/dotnet/core/compatibility/8.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json)
    - [.NET 7](https://learn.microsoft.com/en-us/dotnet/core/compatibility/7.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json)
- [Introducing .NET Aspire: Simplifying Cloud-Native Development with .NET 8](https://devblogs.microsoft.com/dotnet/introducing-dotnet-aspire-simplifying-cloud-native-development-with-dotnet-8/)
- [Performance Improvements in ASP.NET Core 8](https://devblogs.microsoft.com/dotnet/performance-improvements-in-aspnet-core-8/)
- [Performance Improvements in .NET 8](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/)

| Titre                                   | Niveau | Traité |
|-----------------------------------------|--------|--------|
| [Benchmarking Setup](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#benchmarking-setup)                      | 1      | :heavy_check_mark:    |
| [JIT](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#jit)                                     | 1      | :construction:    |
|   - [Tiering and Dynamic PGO](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#tiering-and-dynamic-pgo)             | 2      | :heavy_check_mark:     |
|   - [Vectorization](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#vectorization)                       | 2      | :heavy_check_mark:     |
|   - [Branching](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#branching)                         | 2      | :construction:    |
|   - [Bounds Checking](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#bounds-checking)                   | 2      | ❌    |
|   - [Constant Folding](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#constant-folding)                 | 2      | ❌    |
|   - [Non-GC Heap](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#non-gc-heap)                       | 2      | ❌    |
|   - [Zeroing](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#zeroing)                           | 2      | ❌    |
|   - [Value Types](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#value-types)                      | 2      | ❌    |
|   - [Casting](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#casting)                          | 2      | ❌    |
|   - [Peephole Optimizations](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#peephole-optimizations)           | 2      | ❌    |
| [Native AOT](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#native-aot)                              | 1      | ❌    |
| [VM](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#vm)                                      | 1      | ❌    |
| [GC](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#gc)                                      | 1      | ❌    |
| [Mono](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#mono)                                    | 1      | ❌    |
| [Threading](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#threading)                              | 1      | ❌    |
|   - [ThreadStatic](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#threadstatic)                    | 2      | ❌    |
|   - [ThreadPool](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#threadpool)                    | 2      | ❌    |
|   - [Tasks](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#tasks)                              | 2      | ❌    |
|   - [Parallel](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#parallel)                          | 2      | ❌    |
| [Reflection](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#reflection)                           | 1      | ❌    |
| [Exceptions](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#exceptions)                           | 1      | ❌    |
| [Primitives](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#primitives)                           | 1      | ❌    |
|   - [Enums](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#enums)                             | 2      | ❌    |
|   - [Numbers](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#numbers)                           | 2      | ❌    |
|   - [DateTime](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#datetime)                         | 2      | ❌    |
|   - [Guid](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#guid)                             | 2      | ❌    |
|   - [Random](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#random)                           | 2      | ❌    |
| [Strings, Arrays, and Spans](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#strings-arrays-and-spans) | 1      | ❌    |
|   - [UTF8](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#utf8)                             | 2      | ❌    |
|   - [ASCII](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#ascii)                            | 2      | ❌    |
|   - [Base64](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#base64)                           | 2      | ❌    |
|   - [Hex](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#hex)                            | 2      | ❌    |
|   - [String Formatting](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#string-formatting)         | 2      | ❌    |
|   - [Spans](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#spans)                             | 2      | ❌    |
|   - [SearchValues](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#searchvalues)                 | 2      | ❌    |
|   - [Regex](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#regex)                             | 2      | ❌    |
|   - [Hashing](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#hashing)                          | 2      | ❌    |
|   - [Initialization](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#initialization)               | 2      | ❌    |
|   - [Analyzers](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#analyzers)                      | 2      | ❌    |
| [Collections](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#collections)                       | 1      | ❌    |
|   - [General](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#general)                       | 2      | ❌    |
|   - [List](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#list)                          | 2      | ❌    |
|   - [LINQ](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#linq)                          | 2      | ❌    |
|   - [Dictionary](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#dictionary)                    | 2      | ❌    |
|   - [Frozen Collections](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#frozen-collections)           | 2      | ❌    |
|   - [Immutable Collections](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#immutable-collections)        | 2      | ❌    |
|   - [BitArray](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#bitarray)                       | 2      | ❌    |
|   - [Collection Expressions](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#collection-expressions)      | 2      | ❌    |
| [File I/O](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#file-i-o)                              | 1      | ❌    |
| [Networking](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#networking)                            | 1      | ❌    |
|   - [Networking Primitives](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#networking-primitives)       | 2      | ❌    |
|   - [Sockets](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#sockets)                          | 2      | ❌    |
|   - [TLS](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#tls)                              | 2      | ❌    |
|   - [HTTP](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#http)                             | 2      | ❌    |
| [JSON](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#json)                                     | 1      | ❌    |
| [Cryptography](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#cryptography)                         | 1      | ❌    |
| [Logging](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#logging)                              | 1      | ❌    |
| [Configuration](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#configuration)                         | 1      | ❌    |
| [Peanut Butter](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#peanut-butter)                        | 1      | ❌    |
| [What’s Next?](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#whats-next)                         | 1      | ❌    |
