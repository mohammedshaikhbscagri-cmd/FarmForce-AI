import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class RoleSelectionScreen extends StatelessWidget {
  const RoleSelectionScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Who are you? / आप कौन हैं?')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('I am a...', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 32),
            _RoleCard(
              emoji: '👨‍🌾',
              title: 'I am a Farmer',
              subtitle: 'मैं एक किसान हूँ',
              onTap: () => context.go('/profile-setup'),
            ),
            const SizedBox(height: 16),
            _RoleCard(
              emoji: '👷',
              title: 'I am a Worker',
              subtitle: 'मैं एक मजदूर हूँ',
              onTap: () => context.go('/profile-setup'),
            ),
          ],
        ),
      ),
    );
  }
}

class _RoleCard extends StatelessWidget {
  final String emoji, title, subtitle;
  final VoidCallback onTap;

  const _RoleCard({required this.emoji, required this.title, required this.subtitle, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Row(
            children: [
              Text(emoji, style: const TextStyle(fontSize: 48)),
              const SizedBox(width: 16),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(title, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                  Text(subtitle, style: const TextStyle(fontSize: 14, color: Colors.grey)),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
