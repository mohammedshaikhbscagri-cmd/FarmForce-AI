import 'package:flutter/material.dart';

class WorkerJobDetailScreen extends StatelessWidget {
  const WorkerJobDetailScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Job Details')),
      body: const Center(child: Text('Job details + Accept Job button\n(TODO: Implement)')),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {},
        label: const Text('Accept Job'),
        icon: const Icon(Icons.check),
      ),
    );
  }
}
