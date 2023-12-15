# Le déploiement _Native AOT_

Lorsque une application est déployé en mode _Native AOT_, l'IL code est compilé directement en code natif pour la plateforme cible et contient toutes les dépendances nécessaires pour s'exécuter de manière autonome. Par conséquent les applications _Native AOT_ n'utilisent pas le compilateur JIT (Just-In-Time) et ne bénéficient donc pas de l'optimisation dynamique du code.

Les applications _Native AOT_ **démarreront plus rapidement** et utiliseront moins de mémoire. En outre, ces applications peuvent tourner sur des plateformes qui ne disposent pas d'une installation du _runtime_ .NET Core. Le déploiement _Native AOT_ est donc particulièrement adapté dans le cadre d'application distribuées avec un très grand nombre d'instances comme les infrastructures micro-services.

Le déploiement _Native AOT_ utilise un compilateur ahead-of-time (AOT) pour compiler l'IL code en code natif.

> :bulb: Note
>
> On sent dans la littérature que les applications _Native AOT_ ont été faite pour la conteneurisation. En .NET 7 seule les applications console été supportées. En .NET 8, les applications ASP.NET Core ont été ajoutées, mais uniquement celles de types Web API (en opposition aux Web App), ce qui démontre bien l'intérêt de ce mode de déploiement pour les infrastructures micro-services.

## Les limitation du déploiement _Native AOT_

Le déploiement _Native AOT_ est supporté en .NET 8 pour les projets Console et ASP.NET Core. Néanmoins, il existe des limitations à prendre en compte :

- Impossible d'utiliser les bibliothèques dynamiques, par exemple `Assembly.Load` ou `Assembly.LoadFrom`.
- Impossible d'utiliser de génération de code dynamique, par exemple `System.Reflection.Emit`.
- les fonctionnalités de _trimming_ ne sont pas toutes supportées.

De manière générale, la limitations se situe sur tout ce qui est dynamique et l'utilisation des fonctionnalités du _runtime_ .NET Core.

De même certaines fonctionnalité de diagnostiques et de debug ne sont pas supportées (cf. [Diagnostics and instrumentation](https://learn.microsoft.com/en-us/dotnet/core/deploying/native-aot/diagnostics)).

Les platformes supportées sont x64 et ARM64 sur Windows, Linux et macOS.

## ASP.NET Core en mode _Native AOT_

https://learn.microsoft.com/en-us/aspnet/core/fundamentals/native-aot?view=aspnetcore-8.0
