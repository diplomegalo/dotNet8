# Breaking changes

La liste est basée sur la documentation officielle de Microsoft des _breaking changes_ [.NET 7](https://learn.microsoft.com/en-us/dotnet/core/compatibility/7.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json) et [.NET 8](https://learn.microsoft.com/en-us/dotnet/core/compatibility/8.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json). Cette liste détermine si un _breaking change_ est de type :

- **Source** : impacte le code source, le compilateur Roslyn ne sera affichera une erreur.
- **Assembly** : impacte les références des dll et par conséquent demande une recompilation.
- **Behavior** : impacte le comportement de la fonctionnalité.

La colonne probabilité du tableau ci-dessous indique s'il existe un haut (:warning:) ou un faible (:large_blue_circle:) potentiel d'impact sur les développements courant. Autrement dit s'il est fort ou peu probable de rencontrer ce breaking change. Cette évaluation est arbitraire et basée sur l'expérience personnelle. De même, certains _breaking changes_ ont été mis à l'écart de cette liste, car très spécifique à l'utilisation d'un point en particulier du framework.

## ASP .NET Core

### .NET 8

| Breaking Change | Probabilité | Desc |
| -- | -- | -- |
| [Custom converters for serialization removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/problemdetails-custom-converters)   | :warning: | Impacte le **comportement** de désérialisation des erreurs HTTP vers la classe `ValidationProblemDetail` avec le `JsonStringEnumConverter` au préalable la propriété `Status` contenait la valeur `400` après désérialisation, actuellement elle contient `null`. Typiquement on retrouve ces traitements dans des clients HTTP créé sous forme de Nuget ou de projets _Common/Helper/Tool_ fait sur mesure pour un projet. |
| [TrimMode defaults to full for Web SDK projects](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/trimmode-full) | :large_blue_circle: | Impacte le **_publish_** d'une application ayant une référence vers le MSBuild `Microsoft.NET.Sdk.Web` et `PublishTrimmed=true` dans le `csproj`. La valeur par défaut de `TrimMode` a été modifié à `full` au lieu de `partial`. Les applications ayant des warnings concernant le _trim_ tomberont en erreurs lors du build. |  
| [ConcurrencyLimiterMiddleware is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/concurrencylimitermiddleware-obsolete) | :large_blue_circle: | Impacte le **code source**. Le `ConcurrencyLimiterMiddleware` est un middleware dans ASP.NET Core qui permet de limiter le nombre de requêtes simultanées traitées par une application, aidant ainsi à prévenir les problèmes liés à la concurrence excessive.|
| [ISystemClock is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/isystemclock-obsolete) | :large_blue_circle: | Impacte le **code source**. `ISystemClock` est une interface dans ASP.NET Core utilisée pour obtenir l'heure actuelle du système. Cette classe est maintenant obsolète et remplacé par `TimeProvider`. Il est important de savoir que la signature de la classe et des méthodes est complètement différente. |  
| [Rate-limiting middleware requires AddRateLimiter](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/addratelimiter-requirement)    | :large_blue_circle: | Impacte le **`program.cs`**. L'utilisation du middleware `UseRateLimiter` requiert que les services adéquats soient ajoutés au préalable avec la méthode `AddRateLimiter` |  
| [Security token events return a JSonWebToken](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/securitytoken-events) | :large_blue_circle:         | Impacte **la gestion des JWT**. Lors du mécanisme de gestion du JWT la propriété exposé contenant le token est de type abstrait `SecurityToken`. Au préalable, la class concrète était `JwtSecurityToken`. En .NET8 le type concret est un `JsonWebToken`. Ce _breaking change_ n'a d'impacte que si le code gère le type concret.|

### .NET 7

:construction: En cours de rédaction

## Core .NET Librairies

:construction: En cours de rédaction

## Extensions

:construction: En cours de rédaction

## SDK and MSBuild

:construction: En cours de rédaction

## Serialization

:construction: En cours de rédaction

## EF Core

:construction: En cours de rédaction

## Deployment

:construction: En cours de rédaction

## Globalization

:construction: En cours de rédaction