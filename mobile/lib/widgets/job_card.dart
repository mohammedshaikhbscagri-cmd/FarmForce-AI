import 'package:flutter/material.dart';
import '../models/job_model.dart';

class JobCard extends StatelessWidget {
  final JobModel job;
  final VoidCallback? onTap;

  const JobCard({super.key, required this.job, this.onTap});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(children: [
                    const Icon(Icons.agriculture, color: Color(0xFF2E7D32)),
                    const SizedBox(width: 8),
                    Text(job.taskType, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                  ]),
                  if (job.urgency == 'URGENT')
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                      decoration: BoxDecoration(color: Colors.red, borderRadius: BorderRadius.circular(4)),
                      child: const Text('URGENT', style: TextStyle(color: Colors.white, fontSize: 12)),
                    ),
                ],
              ),
              const SizedBox(height: 8),
              Text('${job.cropType} | ${job.workersNeeded} workers needed', style: const TextStyle(color: Colors.grey)),
              const SizedBox(height: 8),
              Row(children: [
                const Icon(Icons.location_on, size: 16, color: Colors.grey),
                Text('${job.village}, ${job.district}', style: const TextStyle(color: Colors.grey)),
                const Spacer(),
                Text('₹${job.wagePerDay}/day', style: const TextStyle(fontWeight: FontWeight.bold, color: Color(0xFF2E7D32), fontSize: 16)),
              ]),
              const SizedBox(height: 8),
              Text('${job.startDate} — ${job.endDate}', style: const TextStyle(fontSize: 12, color: Colors.grey)),
            ],
          ),
        ),
      ),
    );
  }
}
