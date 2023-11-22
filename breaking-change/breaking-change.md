# Breaking changes

La liste est basée sur la documentation officielle de Microsoft des _breaking changes_ [.NET 7](https://learn.microsoft.com/en-us/dotnet/core/compatibility/7.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json) et [.NET 8](https://learn.microsoft.com/en-us/dotnet/core/compatibility/8.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json). Cette liste détermine si un _breaking change_ est de type :

- **Source** : impacte le code source, le compilateur Roslyn ne sera affichera une erreur.
- **Assembly** : impacte les références des dll et par conséquent demande une recompilation.
- **Behavior** : impacte le comportement de la fonctionnalité.

La colonne probabilité du tableau ci-dessous indique s'il existe un haut (:warning:) ou un faible (:large_blue_circle:) potentiel d'impact sur les développements courant. Autrement dit s'il est fort ou peu probable de rencontrer ce breaking change. Cette évaluation est arbitraire et basée sur l'expérience personnelle. De même, certains _breaking changes_ ont été mis à l'écart de cette liste, car très spécifique à l'utilisation d'un point en particulier du framework.

## ASP .NET Core (.NET 8)

| Breaking Change | Probabilité | Desc |
| -- | -- | -- |
| [Custom converters for serialization removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/problemdetails-custom-converters)   | :warning: | Impacte le **comportement** de désérialisation des erreurs HTTP vers la classe `ValidationProblemDetail` avec le `JsonStringEnumConverter` au préalable la propriété `Status` contenait la valeur `400` après désérialisation, actuellement elle contient `null`. Typiquement on retrouve ces traitements dans des clients HTTP créé sous forme de Nuget ou de projets _Common/Helper/Tool_ fait sur mesure pour un projet. |
| [TrimMode defaults to full for Web SDK projects](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/trimmode-full) | :large_blue_circle: | Impacte le **_publish_** d'une application ayant une référence vers le MSBuild `Microsoft.NET.Sdk.Web` et `PublishTrimmed=true` dans le `csproj`. La valeur par défaut de `TrimMode` a été modifié à `full` au lieu de `partial`. Les applications ayant des warnings concernant le _trim_ tomberont en erreurs lors du build. |  
| [ConcurrencyLimiterMiddleware is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/concurrencylimitermiddleware-obsolete) | :large_blue_circle: | Impacte le **code source**. Le `ConcurrencyLimiterMiddleware` est un middleware dans ASP.NET Core qui permet de limiter le nombre de requêtes simultanées traitées par une application, aidant ainsi à prévenir les problèmes liés à la concurrence excessive.|
| [ISystemClock is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/isystemclock-obsolete) | :large_blue_circle: | Impacte le **code source**. `ISystemClock` est une interface dans ASP.NET Core utilisée pour obtenir l'heure actuelle du système. Cette classe est maintenant obsolète et remplacée par `TimeProvider`. Il est important de savoir que la signature de la classe et des méthodes est complètement différente. |  
| [Rate-limiting middleware requires AddRateLimiter](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/addratelimiter-requirement)    | :large_blue_circle: | Impacte le **`program.cs`**. L'utilisation du middleware `UseRateLimiter` requiert que les services adéquats soient ajoutés au préalable avec la méthode `AddRateLimiter` |  
| [Security token events return a JSonWebToken](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/securitytoken-events) | :large_blue_circle:         | Impacte **la gestion des JWT**. Lors du mécanisme de gestion du JWT la propriété exposée contenant le token est de type abstrait `SecurityToken`. Au préalable, la class concrète était `JwtSecurityToken`. En .NET8 le type concret est un `JsonWebToken`. Ce _breaking change_ n'a d'impacte que si le code gère le type concret.|

## ASP .NET Core (.NET 7)

| Breaking Change | Probabilité | Desc |
| -- | -- | -- | 
| [ASPNET-prefixed environment variable precedence](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/environment-variable-precedence)  | :warning: | Impacte les **pipelines d'intégration et déploiement continu**. La modification porte sur les variables d'environnement préfixé de `ASPNET` et `DOTNET`. Au préalable les valeurs des variables d'environnement préfixé de `ASPNET` écrasé les arguments passés en ligne de commande et les variables préfixées de `DOTNET`. Actuellement c'est l'inverse. |
| [AuthenticateAsync for remote auth providers](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/authenticateasync-anonymous-request) | :warning: | Impacte le **traitement d'authentification**. L'utilisation de la méthode [AuthenticationHttpContextExtensions.AuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.authenticateasync?view=aspnetcore-8.0) renvoi AuthenticateResult.NoResult plutôt qu'une erreur lorsque l'identité de l'utilisateur courant est anonyme. |
| [Middleware no longer defers to endpoint with null request delegate](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/middleware-null-requestdelegate) | :warning: | Ceci impacte le **traitement des requêtes**. Les middlewares de type _file-serving_, comme par exemple `UseStaticFiles` ne délégueront plus le traitement de la requête au middleware suivant si la propriété `RequestDelegate` du endpoint est vide. Ceci a pour conséquence de forcer le `AuthorizationMiddleware` de traiter l'autorisation avant de que le `StaticFileMiddleware` ne renvoie les fichiers demandés. Autrement dit, ce change n'a pas d'impacte si l'`AuthorizationMiddleware` est présent dans le `program.cs` avant les _file-serving_ middlewares. |
| [Output caching API changes](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/output-caching-renames) | :warning: | Impacte **la signature de méthodes** dans le namespace `Microsoft.AspNetCore.OutputCaching`. Certaines API ont été renommées ou supprimées. |

## Core .NET Librairies (.NET 8)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [API obsoletions with non-default diagnostic IDs (.NET 8)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/obsolete-apis-with-custom-diagnostics) | :warning: | Impacte le **code source**. Plusieurs API apparaîtront comme obsolètes et seront marquées en erreur lors de la compilation. |  
| [Backslash mapping in Unix file paths](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/file-path-backslash) | :warning: | Impacte le **traitement des chemins d'accès**. Avec .NET 8, le CoreCLR runtime ne convertit plus automatiquement les `\` en `/` sur les systèmes Unix. Attention de bien prendre en compte les différents environnements : machine locale, environnement de build, de (unit) test et de déploiement. |  
| [Base64.DecodeFromUtf8 methods ignore whitespace](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/decodefromutf8-whitespace) | :warning: | Impacte **le traitement des erreurs de décodage en base 64**. Les espaces contenus dans les valeurs passées en paramètre des méthodes `Base64.DecodeFromUtf8` et `Base64.DecodeFromUtf8InPlace` sont ignorés et ne retournent plus d'erreurs.                                            |  
| [FileStream writes when the pipe is closed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/filestream-disposed-pipe) | :large_blue_circle: | Impacte **le traitement des erreurs lors de l'écriture sur un `FileStream`**. Auparavant, si l'on écrivait sur un `FileStream`, mais que celui-ci était fermé, celui-ci ne levait aucune erreur et aucune donnée n'était écrite. Actuellement, une erreur est levée si l'on tente d'écrire sur un `FileStream` fermé. |  
| [Boolean-backed enum type support removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/bool-backed-enum) | :large_blue_circle: | Impacte **le traitement de _parsing_ vers un _boolean-backed_ enum**. Un _boolean-backed_ enum en .NET est une énumération dont les valeurs sous-jacentes sont de type booléen. Cette opération n'est plus possible en .NET 8 |  
| [GC.GetGeneration might return Int32.MaxValue](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/getgeneration-return-value) | :large_blue_circle: | Le comportement de la méthode `GC.GetGeneration` a été modifié et peut renvoyer un `Int32.MaxValue`. |  
| [# GetFolderPath behavior on Unix](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/getfolderpath-unix) | :large_blue_circle:      | Impacte le **comportement de la méthode `Environnement.GetFolderPath`**. Les valeurs des chemins d'accès des _special folder_ retournées sous Linux, MacOS et Android ont été modifiées.  |  

## Core .NET Librairies (.NET 7)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [API obsoletions with default diagnostic ID (.NET 7)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/obsolete-apis-with-default-diagnostic) | :warning: | Impacte le **code source**. Plusieurs API apparaîtront comme obsolètes et seront marquées en erreur lors de la compilation. |  
| [API obsoletions with non-default diagnostic IDs (.NET 7)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/obsolete-apis-with-custom-diagnostics) | :warning:          | Impacte le **code source**. Plusieurs API apparaîtront comme obsolètes et seront marquées en erreur lors de la compilation. |  
| [DateTime addition methods precision change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/datetime-add-precision) | :warning: | Impacte **le traitement de la méthode `DateTime.AddDays(double)`**. En .NET 8, la précision du paramètre de type `double` est prise dans sa totalité. Les résultats peuvent donc être sensiblement différents. |  
| [Library support for older frameworks](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/old-framework-support) | :warning: | Impacte **les versions des framework .NET minimum supportés** : .NET Framework 4.6.2 / .NET 6 / .NET Standard 2.0 |  
| [Changes to reflection invoke API exceptions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/reflection-invoke-exceptions) |  :large_blue_circle:         | Impacte le **comportement de la méthode `Invoke()`**.Auparavant, la méthode pouvait renvoyer plusieurs types d'exceptions. Actuellement seule la `TargetInvocationException` est levée en cas d'erreur. |  

## Extensions (.NET 8)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [ConfigurationBinder throws for mismatched value](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/configurationbinder-exceptions)| :warning: | Impacte le **comportement du `ConfigurationBinder`** est plus spécifiquement des méthodes `Bind(IConfiguration, Object, Action<BinderOptions)`, `Get<T>(IConfiguration, Action<BinderOption>)` et `Get(IConfiguration, Type, Action<BinderOption>)`. Auparavant, si le `BinderOptions.ErrorOnUnknownConfiguration` était à `true`, une erreur était remontée uniquement si une valeur de la configuration manquait dans le modèle dans lequel était transposé les valeurs. Actuellement, une erreur est également levée si une valeur de la configuration ne peut pas être convertie dans le même type que le modèle.   |
| [Empty keys added to dictionary by configuration binder](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/dictionary-configuration-binding) | :large_blue_circle: | Impacte le **comportement du `ConfigurationBinder`**. Auparavant, les propriétés de configuration n'ayant pas de valeur n'étaient pas transposées dans les dictionnaires (ou map). Actuellement, même les propriétés de configuration n'ayant pas de valeur sont transposées dans les dictionnaires avec la valeur par défaut du type. |
| [ActivatorUtilities.CreateInstance behaves consistently](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/activatorutilities-createinstance-behavior) | :large_blue_circle:          | Impacte le comportement de la méthode `CreateInstance`. Actuellement, la méthode tente de trouver le constructeur avec le plus de paramètres qui correspond à la liste de paramètre en premier (basé sur le comportement : [IServiceProviderIsService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iserviceproviderisservice).). |

## SDK and MSBuild (.NET 8)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [Version requirements for .NET 8 SDK](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/version-requirements) | :warning: | Impacte **les versions minimum supportées des SDK .NET** : Visual Studio & MSBuild 17.7      |
| ['dotnet pack' uses Release configuration](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-pack-config) | :warning: | Impacte le **comportement de production d'un package**. Dorénavant, c'est la configuration release qui est utilisé par défaut. |  
| ['dotnet publish' uses Release configuration](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-publish-config) | :warning: |  Impacte le **comportement de publication d'une application**. Dorénavant, c'est la configuration release qui est utilisé par défaut. |  
| ['dotnet restore' produces security vulnerability warnings](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-restore-audit) | :large_blue_circle: | Impacte le comportement **de build** notamment dans les pipelines de build ou déploiement qui ont le paramètre `<TreatWarningAsErrors` activé. La commande `dotnet restore` peut produire des _warning_ de sécurités.|

## SDK and MSBuild (.NET 7)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |
| [# Solution-level `--output` option no longer valid for build-related commands](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/7.0/solution-level-output-no-longer-valid) | :warning:          | Impacte les commandes du `dotnet` CLI de build, déploiement, publication, etc. L'option `--output/-o` n'est plus supporté. |  

## Serialization (.NET 8)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [Reflection-based deserializer resolves metadata eagerly](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/8.0/metadata-resolving)  | :warning: | Impacte **le traitement de dé-sérialisation des API de `System.Text.Json`**. Il n'y a plus de _lazy resolving_ lors de la dé-sérialisation. Ceci implique que des propriétés qui auparavant n'était pas immédiatement "résolues", le sont en .NET 8 ce qui peut provoquer des comportements ou des erreurs inattendues. |

## Serialization (.NET 7)

| Breaking Change | Probabilité | Desc|  
| -- | -- | -- | 
| [Polymorphic serialization for object types](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/polymorphic-serialization) | :large_blue_circle: | Impacte **le traitement de sérialisation**. Si un `JsonConverter<T>` est définie dans les `JsonSerializerOptions`, l'appel à la méthode `JsonSerializer.Serialize<T>(string, JsonSerializerOptions)` fera appel à celui-ci au détriment du polymorphisme. |
| [JsonSerializerOptions copy constructor includes JsonSerializerContext](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/jsonserializeroptions-copy-constructor) | :large_blue_circle: | Impacte **le comportement des API de sérialisation de `System.Text.Json`**. Le traitement _behind the scene_ de la méthode `JsonSerializer.Serialize(object, JsonSerializerContext)` peut lever une `InvalidOperationException` si le `JsonSerializerContext` n'est pas correctement défini avec le bon type. Auparavant, l'erreur n'était pas levée. |

>:spiral_notepad: Note
>
> Les changements concernant la sérialisation en .NET 7 sont centrés sur l'utilisation des `JsonSerializerOptions` et `JsonSerializerContext`, surtout au niveau des comportements "auto-magique" de conversion de type et de la gestion des `JsonConverter<T>`. Il est important de bien tester les méthodes contenant des actions de sérialisations et dé-sérialisation de manière à valider la rétrocompatibilité de celles-ci.

## EF Core (.NET 8)

| Breaking Change | Probabilité | Desc |  
| -- | -- | ------------------------------------------------------- |  
| [SQL Server date and time now scaffold to .NET DateOnly and TimeOnly](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-8.0/breaking-changes?toc=%2Fdotnet%2Fcore%2Fcompatibility%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json#sqlserver-date-time-only)  | :large_blue_circle: | Impacte le **comportement de scaffolding**. Les types utilisés lors du _scaffold_ des dates sont `DateOnly` et `TimeOnly` au lieu de `DateTime` et `TimeSpan`. |

## EF Core (.NET 7)

| Breaking Change  | Probabilité | Desc |  
| -- | -- | --- |  
| [Encrypt defaults to true for SQL Server connections](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-7.0/breaking-changes?toc=%2Fdotnet%2Fcore%2Fcompatibility%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json&tabs=v7#encrypt-true) | :warning: | Impacte **la méthode de connexion à la DB**. La propriété `Encrypt` de la _connection string_ est maintenant à `true` par défaut. Par conséquent le serveur de base de données doit être configuré avec un certificat valide et le client / application appelante doit _truster_ celui-ci. À noter que cette opération est automatique concernant les déploiements d'application avec une base de données dans Azure. |

## Deployment (.NET7)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [All assemblies trimmed by default](https://learn.microsoft.com/en-us/dotnet/core/compatibility/deployment/7.0/trim-all-assemblies) | :warning: | Impacte le **_publish_ des applications console**.Les Consoles app seront maintenant publiées trimmées par défaut. S’il y avait des warnings liés aux trim, le publish échouera àpd de .NET7.0. Attention, Newtonsoft.Json par exemple ne supporte pas le trimming. |

## Globalization (.NET7)

| Breaking Change | Probabilité | Desc |  
| -- | -- | -- |  
| [Globalization APIs use ICU libraries on Windows Server 2019](https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/7.0/icu-globalization-api) | :large_blue_circle: | Impacte **le déploiement des applications**. Les API `Globalization` utilisent la librairie ICU. Celle-ci devrait être installée par défaut sur les serveurs Windows 2019, mais le passage à ICU peut apporter quelques différences au niveau du [symbole des _currency_](https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/7.0/icu-globalization-api#currency-symbol).|
