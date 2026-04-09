// Quando geramos um app hello world no flutter ele coloca todo o código em um arquivo main.dart
import 'package:flutter/material.dart';
//Para casa: gerar aplicativo de hello world traduzir os comentários e ler o código
// Para casa: baseado no exemplo de hello world, criar uma aplicação que faz o cálculo de IMC em uma tela só, trazer pronto para a aula de laboratório. Tarefa 2: Tentar criar uma aplicação em flutter chamada calculadora eo layout seja uma tela só com o visor dos botões e o controlador de estados faça uso de todas as classes que o professor criou com você
void main() {
  // Toda aplicação em flutter tem um ponto de entrada main e nesse main tem a chamada de uma função nativa do flutter, que você não escreveu, chamada runApp. Ao chmar runApp, o parâmetro que ela espera é uma instância de um widget, de preferência StatelessWidget.
  // runApp espera a instância de uma classe que representa a aplicação toda.
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});



  // Esse widget é a raiz do aplicativo
  @override
  // Contexto de execução: uma aplicação de flutter é uma árvore de widget, então o contexto gerencia essa árvore de widget.
  // O que é gerenciar? É simplesmente cuidar do estado de cada widget que existe na aplicação, todo widget tem o método build, esse método build serve para construi-lo e por fim, coloca-lo na árvore junto com os demais.
  Widget build(BuildContext context) {
    // No método build da classe MyApp de exemplo é rotornado um widget do tipo MaterialApp(uma instância da classe MaterialApp)
    return MaterialApp(
      // Quando você usa o paradigma reativo declarativo você economiza memória, por isso não mantemos instâncias fora da declaração
      // No método build da classe principla que representa a aplicação, criamos uma aplicação reativamente e informamos uma instância de quem será a tela principal(parâmentro home)
      title: 'Flutter Demo',
      theme: ThemeData(
        // Esse é o tema da aplicação.
        //
        //TENTE ISSO: Tente roda o aplicativo com o "flutter run". Você vera que
        //a aplicação tem uma toolbar roxa. Então, sem sair da aplicação, tente mudar
        //a seedColor no colorScheme abaixo para Colors.green então use o "hot reload"
        //(salve as mudanças então pressione o botão "hot reload" na IDE com suporte 
        //Flutter, ou aperte "r" se você usa linha de comando para iniciar o aplicativo)
        //
        //Perceba que o contador não voltou a zero; o estado da aplicação não é perdido ao 
        //dar reload. para voltar ao estado inicial utilize o hot reload no lugar.
        //
        //Isso funciona para o código também, não apenas para valores: a maioria das 
        //mudanças no código poder ser testadas apenas com o hot reload.

        colorScheme: .fromSeed(seedColor: Colors.green),
      ),
      home: const MyHomePage(title: 'Felipe'),
    );
  }
}

class MyHomePage extends StatefulWidget {

  const MyHomePage({super.key, required this.title});

  // Este widget serve de página inicial da sua aplicação. Se estiver sem estado, ou seja, 
  // sem o objeto de State (definido abaixo) que contenha campos que afetam como que a 
  // aplicação se parece.
  //
  // Essa classe é a configuração para esse estado. Ela contém os valores (nesse caso o 
  // título) providenciado pelo parente (nesse caso o widget App) e como sera usado no 
  // método de build do State. Campos na sublcasse Widget sempre são marcados como "final".


  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // Uma classe que representa o estado de uma tela separadamente
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // Isso chama o setState e fala o framework do Flutter que algo mudou nesse State, que 
      // faz essa função rodar novamente a build do metodo abaixo para que o display possa 
      // refletir os valores atualizados. Se nós mudamos o _counter sem chamar o setState(), 
      // o metodo da build não seria chamado novamente, e então nada pareceria ter mudado.

      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // Esse método roda novamente toda vez que o setState é chamado, por exemplo como é 
    // feito pelo método _incrementCounter acima.
    //
    // O framework do Flutter é otimizado para facilitar rodar novamento métodos de build 
    // rapidamente, para que você possa reconstruir qualquer coisa que precisar de 
    // atualização ao invés de manualmente ter que mudar as instancias dos widgets.
    return Scaffold(
      appBar: AppBar(
        // TENTE ISSO: Tente mudar a cor aqui para uma cor específica (para Colors.amber, talvez?) e então acione um hot reload para ver a AppBar mudar de cor enquanto outras cores mantém as mesmas. 
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Aqui nós pegamos o valor do objeto MyHomePage que foi criado no método App.build, então usamos ele para colocar o título na nossa apbar.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: .center,
          children: [
            const Text('You have pushed the button this many times:'),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
