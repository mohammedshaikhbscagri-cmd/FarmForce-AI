import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class ProfileSetupScreen extends StatefulWidget {
  const ProfileSetupScreen({super.key});

  @override
  State<ProfileSetupScreen> createState() => _ProfileSetupScreenState();
}

class _ProfileSetupScreenState extends State<ProfileSetupScreen> {
  final _nameController = TextEditingController();
  final _villageController = TextEditingController();
  final _districtController = TextEditingController();
  final _stateController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Setup Profile / प्रोफाइल सेटअप')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            TextField(controller: _nameController, decoration: const InputDecoration(labelText: 'Full Name', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            TextField(controller: _villageController, decoration: const InputDecoration(labelText: 'Village / गाँव', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            TextField(controller: _districtController, decoration: const InputDecoration(labelText: 'District / जिला', border: OutlineInputBorder())),
            const SizedBox(height: 16),
            TextField(controller: _stateController, decoration: const InputDecoration(labelText: 'State / राज्य', border: OutlineInputBorder())),
            const SizedBox(height: 32),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () => context.go('/farmer/home'),
                child: const Text('Continue'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
