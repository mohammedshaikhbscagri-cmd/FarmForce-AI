import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class PostJobScreen extends StatefulWidget {
  const PostJobScreen({super.key});

  @override
  State<PostJobScreen> createState() => _PostJobScreenState();
}

class _PostJobScreenState extends State<PostJobScreen> {
  String? _selectedTask;
  final List<String> _tasks = ['HARVESTING', 'WEEDING', 'SOWING', 'TRANSPLANTING', 'SPRAYING', 'IRRIGATION', 'OTHER'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Post a Job / काम पोस्ट करें')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            DropdownButtonFormField<String>(
              decoration: const InputDecoration(labelText: 'Task Type', border: OutlineInputBorder()),
              value: _selectedTask,
              items: _tasks.map((t) => DropdownMenuItem(value: t, child: Text(t))).toList(),
              onChanged: (v) => setState(() => _selectedTask = v),
            ),
            const SizedBox(height: 16),
            const TextField(decoration: InputDecoration(labelText: 'Crop Type', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            const TextField(keyboardType: TextInputType.number, decoration: InputDecoration(labelText: 'Workers Needed', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            const TextField(keyboardType: TextInputType.number, decoration: InputDecoration(labelText: 'Wage per Day (₹)', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            const TextField(decoration: InputDecoration(labelText: 'Village', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            const TextField(decoration: InputDecoration(labelText: 'District', border: OutlineInputBorder())),
            const SizedBox(height: 32),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton.icon(
                onPressed: () => context.go('/farmer/home'),
                icon: const Icon(Icons.check),
                label: const Text('Post Job'),
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          // TODO: Open voice input for job creation
        },
        child: const Icon(Icons.mic),
      ),
    );
  }
}
