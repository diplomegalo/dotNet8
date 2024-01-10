---
title: NuGet signed-package verification
description: dotnet restore prend beaucoup de temps à s'exécuter sur un serveur ubuntu 22.04.
tags: [dotnet cli, nuget, restore, CLR, signed-package, ubuntu]
---
# NuGet signed-package verification

## Problème

Durant l'exécution du pipeline de build, l'étape du `dotnet restore` prenait près de 30 min pour s'exécuter.

Le pipeline de build est exécuté sur un serveur ubuntu 22.04.

## Recherche

Depuis la version 8.0 le restore des packages NuGet vérifie le CLR des packages signé _online_. Le serveur de build n'avait pas accès à internet et le restore des packages NuGet prenait donc beaucoup de temps.

[NuGet signed-package verification](https://learn.microsoft.com/en-us/dotnet/core/tools/nuget-signed-package-verification#linux).

## Solution

> La solution n'a pas encore été trouvée. Intuitivement, il faudrait permettre aux serveurs de scalset d'accéder aux serveurs de vérification, mais malheureusement ces serveurs ne sont pas connu.

### Alternative : Set de variables d'environnement

Il est possible de désactiver la vérification des packages signés en settant la variable `DOTNET_NUGET_SIGNATURE_VERIFICATION` à `false`. Attention néanmoins qu'avec cette solution vous bypassez le system de vérification des packages. Ceci ouvre donc un problème potentiel de sécurité.
