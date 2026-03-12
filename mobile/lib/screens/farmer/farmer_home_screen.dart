import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class FarmerHomeScreen extends StatelessWidget {
  const FarmerHomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('FarmForce AI — Farmer')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Dashboard', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            Row(children: [
              _StatCard(title: 'Active Jobs', value: '3', icon: Icons.work),
              const SizedBox(width: 12),
              _StatCard(title: 'Workers Hired', value: '12', icon: Icons.people),
            ]),
            const SizedBox(height: 12),
            Row(children: [
              _StatCard(title: 'Total Spent', value: '₹18,500', icon: Icons.currency_rupee),
              const SizedBox(width: 12),
              _StatCard(title: 'Avg Rating', value: '4.7 ⭐', icon: Icons.star),
            ]),
            const SizedBox(height: 24),
            const Text('Quick Actions', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            Wrap(spacing: 12, runSpacing: 12, children: [
              _ActionButton(icon: Icons.add_circle, label: 'Post Job', onTap: () => context.go('/farmer/post-job')),
              _ActionButton(icon: Icons.search, label: 'Find Workers', onTap: () => context.go('/farmer/workers')),
              _ActionButton(icon: Icons.book_online, label: 'My Bookings', onTap: () => context.go('/farmer/bookings')),
              _ActionButton(icon: Icons.payment, label: 'Payments', onTap: () => context.go('/farmer/payment')),
            ]),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => context.go('/farmer/post-job'),
        icon: const Icon(Icons.add),
        label: const Text('Post Job'),
      ),
    );
  }
}

class _StatCard extends StatelessWidget {
  final String title, value;
  final IconData icon;
  const _StatCard({required this.title, required this.value, required this.icon});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Card(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Icon(icon, color: const Color(0xFF2E7D32), size: 32),
              const SizedBox(height: 8),
              Text(value, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
              Text(title, style: const TextStyle(fontSize: 12, color: Colors.grey)),
            ],
          ),
        ),
      ),
    );
  }
}

class _ActionButton extends StatelessWidget {
  final IconData icon;
  final String label;
  final VoidCallback onTap;
  const _ActionButton({required this.icon, required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: const Color(0xFF2E7D32).withOpacity(0.1),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Column(
          children: [
            Icon(icon, color: const Color(0xFF2E7D32)),
            const SizedBox(height: 4),
            Text(label, style: const TextStyle(fontSize: 12)),
          ],
        ),
      ),
    );
  }
}
