import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import '../../config/app_constants.dart';

class LanguageSelectionScreen extends StatelessWidget {
  const LanguageSelectionScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Select Language / भाषा चुनें')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: GridView.builder(
          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            childAspectRatio: 2.5,
            crossAxisSpacing: 12,
            mainAxisSpacing: 12,
          ),
          itemCount: supportedLanguages.length,
          itemBuilder: (context, index) {
            final entry = supportedLanguages.entries.elementAt(index);
            return ElevatedButton(
              onPressed: () => context.go('/login'),
              child: Text(entry.value, textAlign: TextAlign.center),
            );
          },
        ),
      ),
    );
  }
}
