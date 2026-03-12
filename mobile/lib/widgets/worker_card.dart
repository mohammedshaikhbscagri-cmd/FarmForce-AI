import 'package:flutter/material.dart';
import '../models/user_model.dart';

class WorkerCard extends StatelessWidget {
  final UserModel worker;
  final double? distanceKm;
  final VoidCallback? onTap;

  const WorkerCard({super.key, required this.worker, this.distanceKm, this.onTap});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              CircleAvatar(
                radius: 30,
                backgroundImage: worker.profilePhotoUrl != null ? NetworkImage(worker.profilePhotoUrl!) : null,
                child: worker.profilePhotoUrl == null ? const Icon(Icons.person, size: 30) : null,
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(worker.name ?? 'Unknown', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                    if (distanceKm != null)
                      Text('${distanceKm!.toStringAsFixed(1)} km away', style: const TextStyle(color: Colors.grey, fontSize: 12)),
                    Row(children: [
                      const Icon(Icons.star, color: Colors.amber, size: 16),
                      Text(worker.avgRating.toStringAsFixed(1), style: const TextStyle(fontWeight: FontWeight.bold)),
                      const SizedBox(width: 8),
                      Text('${worker.totalJobs} jobs', style: const TextStyle(color: Colors.grey, fontSize: 12)),
                    ]),
                  ],
                ),
              ),
              if (worker.isVerified)
                const Icon(Icons.verified, color: Color(0xFF2E7D32), size: 20),
            ],
          ),
        ),
      ),
    );
  }
}
