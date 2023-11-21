# Breaking changes

La liste est basée sur la documentation officielle de Microsoft des _breaking changes_ [.NET 7](https://learn.microsoft.com/en-us/dotnet/core/compatibility/7.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json) et [.NET 8](https://learn.microsoft.com/en-us/dotnet/core/compatibility/8.0?toc=%2Fdotnet%2Ffundamentals%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json). Cette liste détermine si un _breaking change_ est de type :

- **Source** : impacte le code source, le compilateur Roslyn ne sera affichera une erreur.
- **Assembly** : impacte les références des dll et par conséquent demande une recompilation.
- **Behavior** : impacte le comportement de la fonctionnalité.

La colonne probabilité du tableau ci-dessous indique s'il existe un haut (:boom:) ou un faible (:question:) potentiel d'impact sur les développements. Cette évaluation est arbitraire et basée sur l'expérience de l'équipe. De même, certains _breaking changes_ ont été mis à l'écart de cette liste, car très spécifique à l'utilisation d'un point en particulier du framework.

## ASP .NET Core

### .NET 8

| Breaking Change | Probabilité | Desc |
| -- | -- | -- |
| [Custom converters for serialization removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/problemdetails-custom-converters)   | :boom: | La sérialisation de la classe `ValidationProblemDetail`, utile dans la récupération des request HTTP, a été modifié et ne permet plus de _custom converter_. </br></br>Impacte le traitement des erreurs HTTP. Typiquement on retrouve ces traitement dans les helpers / package de traitement des call HTTP. |
| [# TrimMode defaults to full for Web SDK projects](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/trimmode-full)                   | ❓      | Concerne la méthode de _publish_ : `PublishTrimmed=true` |  
| [# ConcurrencyLimiterMiddleware is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/concurrencylimitermiddleware-obsolete) | ❓      | Le `ConcurrencyLimiterMiddleware` est un middleware dans ASP.NET Core qui permet de limiter le nombre de requêtes simultanées traitées par une application, aidant ainsi à prévenir les problèmes liés à la concurrence excessive.|  
| [# ISystemClock is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/isystemclock-obsolete)                                | ❓      | `ISystemClock` est une interface dans ASP.NET Core utilisée pour obtenir l'heure actuelle du système.                                                                                                                                |  
| [# Rate-limiting middleware requires AddRateLimiter](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/addratelimiter-requirement)    | ❓      | Il est maintenant nécessaire d'appeler explicitement la méthode `AddRateLimite`.                                                                                                                                |  
| [# Security token events return a JSonWebToken](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/securitytoken-events)               | ❓         | Le comportement de gestion des de la class [Microsoft.IdentityModel.JsonWebTokens](https://learn.microsoft.com/en-us/dotnet/api/microsoft.identitymodel.jsonwebtokens) change et contient maintenant les propriétés dérivées du `SecurityToken`.                                                                                     |

### .NET 7

| Breaking Change | Probabilité              | Desc |     
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | 
| [# ASPNET-prefixed environment variable precedence](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/environment-variable-precedence)                                   | 💥                       | Utilisation de variables d'env ASPNET-…ou DOTNET-…dans les CI/CD 💥 Si oui avant l'ASPNET-xxx override les DOTNET-xxx aujourd'hui c'est l'inverse |     
| [# AuthenticateAsync for remote auth providers](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/authenticateasync-anonymous-request)                                   | 💥                       | Renvoi AuthenticateResult.NoResult plutôt qu'une erreur lors de l'étape d'authentification et qu'il n'y a pas de current user                                                                         |     |                                                                                  |     
| [# Microsoft.Data.SqlClient updated to 4.0.1](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/microsoft-data-sqlclient-updated-to-4-0-1)                               | 💥                       | Voir EF Core.                                         |     |  
| [# Middleware no longer defers to endpoint with null request delegate](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/middleware-null-requestdelegate)                | 💥 | La propriété requestDelegate du endpoint doit être remplie pour faire passer à un autre middleware. Peut avoir un impact dans l'utilisation du `UseStaticFiles`.          |     
| [# Output caching API changes](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/7.0/output-caching-renames) | 💥 | Impacte l'utilisation du cache. |     

## Core .NET Librairies

### .NET 8

| Breaking Change                                                                                                                                                                                              | Probabilité | Desc                                                              |  
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------- |  
| [# API obsoletions with non-default diagnostic IDs (.NET 8)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/obsolete-apis-with-custom-diagnostics)                    | 💥         | Une série de ressources (*class* ou *method*) sont devenues obsolètes.                                |  
| [# Backslash mapping in Unix file paths](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/file-path-backslash)                                                          | 💥         | Les \\ ne sont plus convertis en / dans les systèmes Linux. Peut avoir un impact lors de l'exécution des tests.        |  
| [# Base64.DecodeFromUtf8 methods ignore whitespace](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/decodefromutf8-whitespace)                                         | 💥         | Les espaces contenus dans les valeurs passées en paramètre des méthodes `Base64.DecodeFromUtf8` et `Base64.DecodeFromUtf8InPlace` sont ignorés et ne retournent plus d'erreurs.                                            |  
| [# FileStream writes when the pipe is closed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/filestream-disposed-pipe)                                                    | ❓      | Changement du type d'exception sur les erreurs levées par `FileStream` |  
| [# Boolean-backed enum type support removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/bool-backed-enum)                                                         | ❓      | Concerne l'énumération d'un booléen.                                                                  |  
| [# GC.GetGeneration might return Int32.MaxValue](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/getgeneration-return-value)                                           | ❓      | Le comportement de la méthode `GC.GetGeneration` a été modifié.                                                                   |  
| [# GetFolderPath behavior on Unix](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/8.0/getfolderpath-unix)                                                                 | ❓      | Il s'agit juste des *path* des `SpecialFolder` sous Linux/MacOS                                         |  

### .NET 7

| Breaking Change                                                                                                                                                                    | Probabilité | Desc                                                                                                                                          |  
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- |  
| [# API obsoletions with default diagnostic ID (.NET 7)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/obsolete-apis-with-default-diagnostic)      | 💥          | Un certain nombre de classes et de méthodes sont devenues obsolètes                                                                          |  
| [# API obsoletions with non-default diagnostic IDs (.NET 7)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/obsolete-apis-with-custom-diagnostics) | 💥          | Un certain nombre de classes et de méthodes sont devenues obsolètes                                                                          |  
| [# DateTime addition methods precision change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/datetime-add-precision)                              | 💥          | La précision du paramètre DateTime.AddDays(double) prend maintenant la totalité du double => les résultats peuvent être sensiblement différent    |  
| [# Library support for older frameworks](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/old-framework-support)                                     | 💥          | Min supporté : .NET Framework 4.6.2 / .NET 6 / .NET Standard 2.0                                                                              |  
| [# Changes to reflection invoke API exceptions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/reflection-invoke-exceptions)                       | ❓          | TargetInvocationException est dans tous les cas levés (si problème), avant il y avait aussi des `NullReferenceException` |  
| [# Legacy FileStream strategy removed](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/7.0/filestream-compat-switch)                                    | ❓          | À voir par application si le `UseNet5CompatFileStream` est utilisé                                                                            |  

## Extensions

### .NET 8

| Breaking Change                                                                                                                                                                              | Probabilité | Desc                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
| [# ActivatorUtilities.CreateInstance behaves consistently](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/activatorutilities-createinstance-behavior)            | 💥          | La méthode [CreateInstance](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.activatorutilities.createinstance) a changé de comportement : elle tente de trouver le constructeur avec le plus de paramètres qui correspond à la liste de paramètre en premier (basé sur le comportement : [IServiceProviderIsService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iserviceproviderisservice).) |  
| [# ConfigurationBinder throws for mismatched value](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/configurationbinder-exceptions)                               | 💥          | Les valeurs non connues ne sont plus passées sous silence, mais provoquent une erreur                                                                                                                                                                                                                                                                                                                                                                                           |  
| [# HostApplicationBuilderSettings.Args respected by HostApplicationBuilder ctor](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/hostapplicationbuilder-ctor)     | 💥          | Peut avoir un impact dans le cadre du CD.                                                                                                                                                                                                                                                                                                                                                                                                                                   |  
| [# Empty keys added to dictionary by configuration binder](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/8.0/dictionary-configuration-binding)                      | 💥          | Peut avoir un impact sur les configurations                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### .NET 7

| Breaking Change                                                                                                                                                                                           | Probabilité | Desc                                                                                                                                                                                         |  
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
| [# Binding config to dictionary extends values](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/7.0/config-bind-dictionary)            | 💥    | Peut avoir un impact dans les configurations |  
| [# Environment variable prefixes](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/7.0/environment-variable-prefix)                    | ❓ | Le comportement pour récupérer / setter des variables d'environnement depuis le code a été modifié                                                                                                                                                                                 |

## SDK and MSBuild

### .NET 8

| Breaking Change                                                                                                                                                             | Probabilité | Desc                                          |  
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------- |  
| [# Version requirements for .NET 8 SDK](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/version-requirements)                                          | 💥          | Min version Visual Studio & MSBuild 17.7      |  
| [# 'dotnet pack' uses Release configuration](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-pack-config)                                        | 💥          | Impact dans le CD                            |  
| [# 'dotnet publish' uses Release configuration](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-publish-config)                                  | 💥          | Impact dans le CD                            |  
| [# 'dotnet restore' produces security vulnerability warnings](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/dotnet-restore-audit)                     | ❓          | Impact dans le CD                            |  
| [# MSBuild custom derived build events deprecated](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/custombuildeventargs)                                | ❓          |                                               |  
| [# MSBuild respects DOTNET_CLI_UI_LANGUAGE](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/msbuild-language)                                           | ❓          | (Lié à l'*encoding* en sorti de la `Console`) |

### .NET 7

| Breaking Change                                                                                                                                                                            | Probabilité | Desc                                  |  
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------------------------- |  
| [# SDK no longer calls ResolvePackageDependencies](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/7.0/resolvepackagedependencies)                                         | 💥          | Impacte le CI / CD.                   |  
| [# BinaryFormatter serialization of custom BuildEventArgs and ITaskItems removed for .NET 7](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/7.0/custom-serialization)     | 💥          | MSBuild ne supporte plus ce mécanisme. |  
| [# Solution-level `--output` option no longer valid for build-related commands](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/7.0/solution-level-output-no-longer-valid) | 💥          | Impacte le CI / CD.                   |  
| [# CLI console output uses UTF-8](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/8.0/console-encoding)                                                                   | ❓          |                                       |

## Serialization

### .NET 8

| Breaking Change                                                                                                                                                       | Probabilité | Desc                                                    |  
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------- |  
| [# Reflection-based deserializer resolves metadata eagerly](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/8.0/metadata-resolving)  | 💥         | Il n'y a plus de lazy resolving, ce qui peut provoquer des comportements ou des erreurs inattendus |

### .NET 7

| Breaking Change                                                                                                                                                                                 | Probabilité | Desc                                                                                                   |  
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------ |  
| [# JsonSerializerOptions copy constructor includes JsonSerializerContext](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/jsonserializeroptions-copy-constructor) | 💥          | À voir par application (changement de signature de méthode)                                            |  
| [# Polymorphic serialization for object types](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/polymorphic-serialization)                                         | 💥          | N'utilise plus jamais le polymorphisme quand deserialize en object et qu'il existe un custom converter |  
| [# System.Text.Json source generator fallback](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/reflection-fallback)                                               | 💥          | Plus de fallback auto-magique si le contexte utilisé n'est pas définie                    |  
| [# BinaryFormatter serialization APIs produce compiler errors](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/binaryformatter-apis-produce-errors)               | ❓          | Fait parti du plan de décommissionnement de cette feature                                              |  
| [# SerializationFormat.Binary is obsolete](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/serializationformat-binary)                                            | ❓          | Fait parti du plan de décommissionnement de cette feature                                              |  
| [# Deserialize Version type with leading or trailing whitespace](https://learn.microsoft.com/en-us/dotnet/core/compatibility/serialization/7.0/deserialize-version-with-whitespace)             | ❓          | Lève une exception lors d'une déserialisation avec une la propriété `Version` vide.                    |

## EF Core

### .NET 8

| Breaking Change                                                                                                                                                       | Probabilité | Desc                                                    |  
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------- |  
| [# SQL Server date and time now scaffold to .NET DateOnly and TimeOnly](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-8.0/breaking-changes?toc=%2Fdotnet%2Fcore%2Fcompatibility%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json#sqlserver-date-time-only)  | ❓         | Les types utilisés lors du *scaffold* des dates sont `DateOnly` et `TimeOnly` au lieu de `DateTime` et `TimeSpan`. |

### .NET 7

| Breaking Change                                                                                                                                                                                           | Probabilité | Desc                                                                                                                                                                                         |  
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --- |  
| [# Encrypt defaults to true for SQL Server connections](https://learn.microsoft.com/en-us/ef/core/what-is-new/ef-core-7.0/breaking-changes?toc=%2Fdotnet%2Fcore%2Fcompatibility%2Ftoc.json&bc=%2Fdotnet%2Fbreadcrumb%2Ftoc.json&tabs=v7#encrypt-true) | 💥 | Encrypt est maintenant à true par défault dans les connectionString, ce qui signifie que le server doit être configuré avec un certificat valide et que le client doit trust ce certificat. Doit être testé par toutes les applications utilisant une DB SQL Server.   |

## Deployment

### .NET7

| Breaking Change                                                                                                                                                                                           | Probabilité | Desc                                                                                                                                                                                         |  
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --- |  
| [# All assemblies trimmed by default](https://learn.microsoft.com/en-us/dotnet/core/compatibility/deployment/7.0/trim-all-assemblies) | 💥 | Les Consoles app seront maintenant publiées trimmée par défaut. si il y avait des warnings liée aux trim, le publish échouera àpd de .NET7.0. Attention, Newtonsoft.Json par exemple ne supporte pas le trimming     |

## Globalization

### .NET7

| Breaking Change                                                                                                                                                                                           | Probabilité | Desc                                                                                                                                                                                         |  
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------- |  
| [# Globalization APIs use ICU libraries on Windows Server 2019](https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/7.0/icu-globalization-api) | 💥   | ICU installé par défaut sur Windows Server 2019, mais le passage à ICU peut apporter quelques différences au niveau du symboles des currency [https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/7.0/icu-globalization-api#currency-symbol](https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/7.0/icu-globalization-api#currency-symbol).|
