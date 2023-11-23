# Amélioration des performances en .NET 8

Cette page est un condensé de la page du blog [Performance Improvements in .NET 8](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/).

>:spiral_notepad: les informations contenue dans cette page de blog sont très denses et demande une certaine compréhension de concepts annexes. L'objectif de cette documentation est de simplifier les concepts pour les rendre accessibles et permettre une compréhension rapide des améliorations de performances de .NET 8. Par conséquent, certains chapitres et concepts seront survolés, voire ignorés (cf. [Non couvert](#non-couvert)).

## Améliorations natives

Les améliorations natives sont inhérentes à la migration de code en .NET 8, autrement dit ces améliorations seront mises en place sans intervention de votre part.

### Dynamic PGO

Pour comprendre le Dynamic PGO, il faut comprendre le fonctionnement de la compilation JIT :

- Le JIT (Just in Time) est le compilateur de code C# en code machine. Il est utilisé par le CLR (Common Language Runtime) pour exécuter le code C#.
- Tier0 et Tier1 sont des états de la compilation JIT. Tier0 est la compilation rapide, Tier1 est la compilation optimisée.

Le Dynamic PGO est une technique de compilation qui permet de compiler le code en deux temps. L'objectif du Dynamic PGO est d'obtenir un code machine optimisé rapidement sans pour autant prendre trop de temps dans l'exécution du programme. Pour se faire, il passe par deux étapes :

- La première est une compilation rapide (Tier0) qui permet d'obtenir un code machine rapidement.
- La deuxième est une compilation optimisée (Tier1) qui permet d'obtenir un code machine optimisé.

Le passage du Tier0 au Tier1 se fait en fonction de l'exécution du programme, de manière concrète les étapes de compilations sont les suivantes :

1. **Tier0 (non optimisé, non instrumentalisé)** : Le code est compilé **rapidement**, mais de manière **non optimisée**. Sur base l'exécution le Dynamic PGO va enregistrer les méthodes les plus utilisées et les plus lentes.
2. **Tier0 (non optimisé, instrumentalisé)** : le Dynamic PGO va injecter des points de mesures dans le code de manière à savoir comment l'optimiser. Cette étape est toujours **non optimisée**, mais **instrumentalisé** (traduit de _instrumented_). Le Dynamic PGO est prêt à optimiser le code sur base des informations qu'il récolte.
3. **Tier1 (optimisé avec Dynamic PGO)**: le code est finalement complètement optimisé.

On peut noter que seules les méthodes fréquemment utilisées et les plus lentes seront optimisées. Par conséquent cette technique d'optimisation permet de se concentrer sur les exécutions les plus coûteuses.

La démo de la **Conf.NET 2023** faite par Stephen Toub : [Dynamic PGO viewed with DOTNET_JitDisasm{summary}](https://www.youtube.com/live/xEFO1sQ2bUc?si=OuZH2HnBmXQPaFJ-) permet de très bien comprendre le phénomène, car on y voit distinctement les étapes de compilation de même que le code assembleur généré par le compilateur dans lequel il est possible de s'apercevoir des optimisations.

### Branching

Les améliorations de performances liées au branching sont liées à l'optimisation des branchements conditionnels : loops, if/else, switch, etc. Les hardwares modernes ont été optimisés pour les branchements conditionnels, par exemple en lisant et décodant l'instruction suivante durant l'exécution de l'instruction courante. Cependant, ceci n'est possible que si l'on sait quelle est l'instruction suivante : le **branch prediction**. Néanmoins, si la prédiction n'est pas bonne, le coup de l'exécution est très élevé. Par conséquent, le meilleur moyen d'optimiser des branchements conditionnels est de les supprimer. La version .NET 8 a été optimisé dans ce sens est permet de supprimer les branchements conditionnels de manière plus efficace.

En outre la version .NET 8 du framework permet d'utiliser des instructions de _move_ conditionnel tels que `cmov` et `csel` (pour les processeurs X86/64 et ARM). Ces instructions permettent de combiner l'évaluation d'une condition et l'assignation d'une valeur à une variable en une fois. De cette manière l'instruction suivante est toujours connue et le _branch prediction_ n'est plus utile.

### Bounds Checking

Le [Bounds Checking](devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#bounds-checking) décrit l'amélioration apporté à .NET 8 concernant la vérification des limites (borne supérieur) d'un Array, d'une string ou d'un Span. En quelque mots, dans des cas bien particuliers,.NET 8 est en mesure de comprendre qu'il n'est pas nécessaire de faire cette vérification, car il est impossible de dépasser l'index maximal, comme par exemple avec l'instruction : `myArray[(uint)hashcode % myArray.Length]`,ayant pour résultat d'épargner du temps de traitement. Dans la vidéo [Hardware Intrinsic in .NET 8](https://youtu.be/mSBsWBKh1-k?si=tuAAeF-aORvMT2ik), l'orateur présente une série de benchmark dont certains montrent la perte de performance dûe à cette étape de _bound checking_.

### Non couvert

Ci-dessous la liste des sous chapitres non couverts.

- La [Vectorization](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-8/#vectorization), car ce sujet est très spécifique au besoin de communiquer avec des processeurs vectoriels, ce qui sort du cadre de mes compétences et des demandes que je reçois dans mon travail.
 

>:spiral_notepad: Toutes personnes désireuses de compléter cette documentation en prenant un des sujets non couverts est la bienvenue. :wink:


## Nouveautés

Les nouveautés sont des améliorations qui ne sont pas appliquées par défaut, mais qui peuvent être implémentées par un développeur.

### SearchValues

Une nouveauté de .NET 8 est la possibilité de rechercher des valeurs dans des tableaux de manière plus efficace avec le type [`SearchValues<T>`](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.searchvalues-1?view=net-8.0&viewFallbackFrom=dotnet-aspire-8.0).

Ci-dessous un exemple de comparaison de recherche de valeurs dans un tableau de `char` :

```csharp
// Before
private static readonly char[] s_values = new [] { 'a', 'b', 'c', 'x', 'y', 'z' };
// ...
int pos = source.IndexOfAny(s_values);

// After
private static readonly SearchValues s_values = SearchValues.Create("abcxyz");
// ...
int pos = source.IndexOfAny(s_values);
```

>:spiral_notepad: Cet exemple est tiré d'une démo faite durant la [.NET Conf 2023](https://www.youtube.com/live/xEFO1sQ2bUc?si=sf9n8_-bpWpptoFq)
