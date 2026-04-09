import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: .fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final double _altura = 1.80, _peso = 80;
  double _imc = 0;

  void _calcularIMC() {
    setState(() {
      _imc = _peso / (_altura * _altura);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: .center,
          children: [
            const Text('Aperte o botão para descobrir o seu IMC;'),
            Text(
              '$_imc',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            FloatingActionButton(
              onPressed: _calcularIMC,
              tooltip: 'Calcular IMC',
              child: const Icon(Icons.verified),)
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _calcularIMC,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
