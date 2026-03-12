import 'package:flutter/material.dart';

class WorkerDiscoveryScreen extends StatelessWidget {
  const WorkerDiscoveryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Find Workers / मजदूर खोजें')),
      body: const Center(
        child: Text('Worker discovery with map + list view\n(TODO: Implement Google Maps + AI matching)'),
      ),
    );
  }
}
