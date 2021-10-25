# Análisis Semántico

![GitHub top language](https://img.shields.io/github/languages/top/SebasRod23/cool-antlr)
![Lines of code](https://tokei.rs/b1/github/SebasRod23/cool-antlr?category=code)

## Autores

<table>
  <tr>
    <td align="center"><a href="https://github.com/KevinTMtz"><img src="https://avatars.githubusercontent.com/u/44516784" width="100px;" alt=""/><br /><sub><b>Kevin Torres Martínez</b></sub></a><br />A01656257</td>
    <td align="center"><a href="https://github.com/SebasRod23"><img src="https://avatars.githubusercontent.com/u/42384931" width="100px;" alt=""/><br /><sub><b>Sebastián Rodríguez Galarza</b></sub></a><br />A01656159</td>
    <td align="center"><a href="https://github.com/SebasRod23"><img src="https://avatars.githubusercontent.com/u/15371718?v=4" width="100px;" alt=""/><br /><sub><b>Víctor Antonio Godínez Rodríguez</b></sub></a><br />A01339529</td>
  </tr>
</table>

## Tree Printer

#### ./input/semantic/basicclassestree.cool

```zsh
  >- AProgram
     |- AClassDecl
     |  |- Main
     |  |- Object
     |  |- AMethodFeature
     |  |  |- main
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 0
     |- AClassDecl
     |  |- A
     |  |- Object
     |  |- AAttributeFeature
     |  |  |- a
     |  |  |- Object
     |  |  |- AIntExpr:Int
     |  |  |  `- 0
     |  |- AAttributeFeature
     |  |  |- b
     |  |  |- Object
     |  |  |- AStrExpr:String
     |  |  |  `-
     |  |- AAttributeFeature
     |  |  |- c
     |  |  |- Object
     |  |  |- ABoolExpr:Bool
     |  |  |  `- true
```

#### ./input/semantic/simplearith.cool

```zsh
  >- AProgram
     |- AClassDecl
     |  |- Main
     |  |- Object
     |  |- AMethodFeature:Object
     |  |  |- main
     |  |  |- Object
     |  |  |- AListExpr:Int
     |  |  |  |- APlusExpr:Int
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 5
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 4
     |  |  |  |- AMinusExpr:Int
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 5
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 4
     |  |  |  |- AMultExpr:Int
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 3
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 2
     |  |  |  |- ADivExpr:Int
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 3
     |  |  |  |  |- AIntExpr:Int
     |  |  |  |  |  `- 2
```

#### ./input/semantic/classes.cool

```zsh
  >- AProgram
     |- AClassDecl
     |  |- A
     |  |- Object
     |  |- AAttributeFeature
     |  |  |- a
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 0
     |  |- AAttributeFeature
     |  |  |- d
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 1
     |  |- AMethodFeature
     |  |  |- f
     |  |  |- Int
     |  |  |- AAssignExpr
     |  |  |  `- a
     |  |  |  |- APlusExpr:Int
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- a
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- d
     |- AClassDecl
     |  |- B
     |  |- A
     |  |- AAttributeFeature
     |  |  |- b
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 2
     |  |- AMethodFeature
     |  |  |- f
     |  |  |- Int
     |  |  |- AObjectExpr:Int
     |  |  |  `- a
     |  |- AMethodFeature
     |  |  |- g
     |  |  |- Int
     |  |  |- AAssignExpr
     |  |  |  `- a
     |  |  |  |- AMinusExpr:Int
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- a
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- b
     |- AClassDecl
     |  |- C
     |  |- A
     |  |- AAttributeFeature
     |  |  |- c
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 3
     |  |- AMethodFeature
     |  |  |- h
     |  |  |- Int
     |  |  |- AAssignExpr
     |  |  |  `- a
     |  |  |  |- AMinusExpr:Int
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- a
     |  |  |  |  |- AObjectExpr:Int
     |  |  |  |  |  `- c
     |- AClassDecl
     |  |- Main
     |  |- Object
     |  |- AMethodFeature
     |  |  |- main
     |  |  |- Int
     |  |  |- AIntExpr:Int
     |  |  |  `- 6
```

## Licencia

Código publicado bajo [MIT License](https://github.com/kevintmtz/MedCLIP/blob/main/LICENSE).
