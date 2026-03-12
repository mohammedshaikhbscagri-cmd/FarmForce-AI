import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class WorkerHomeScreen extends StatelessWidget {
  const WorkerHomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('FarmForce AI — Worker')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              decoration: InputDecoration(
                hintText: 'Search jobs nearby...',
                prefixIcon: const Icon(Icons.search),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
              ),
              onTap: () => context.go('/worker/search'),
            ),
          ),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text('Jobs Near You', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                Text('See All', style: TextStyle(color: Color(0xFF2E7D32))),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: 5,
              itemBuilder: (context, i) => Card(
                child: ListTile(
                  leading: const Icon(Icons.agriculture, color: Color(0xFF2E7D32), size: 40),
                  title: const Text('Wheat Harvesting'),
                  subtitle: const Text('Pune, Maharashtra • 2.3 km'),
                  trailing: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text('₹450/day', style: TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF2E7D32))),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(color: Colors.red, borderRadius: BorderRadius.circular(4)),
                        child: const Text('URGENT', style: TextStyle(color: Colors.white, fontSize: 10)),
                      ),
                    ],
                  ),
                  onTap: () => context.go('/worker/job/1'),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
