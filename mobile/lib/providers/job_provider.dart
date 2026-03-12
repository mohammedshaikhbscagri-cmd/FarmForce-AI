import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/job_model.dart';
import '../config/api_config.dart';
import 'auth_provider.dart';

class JobState {
  final List<JobModel> jobs;
  final bool isLoading;
  final String? error;

  JobState({this.jobs = const [], this.isLoading = false, this.error});
}

class JobNotifier extends StateNotifier<JobState> {
  final apiService;

  JobNotifier(this.apiService) : super(JobState());

  Future<void> fetchJobs({String? taskType, double? minWage, String? district}) async {
    state = JobState(isLoading: true);
    try {
      final params = <String, dynamic>{};
      if (taskType != null) params['task_type'] = taskType;
      if (minWage != null) params['min_wage'] = minWage;
      if (district != null) params['district'] = district;
      final response = await apiService.get(ApiConfig.jobs, params: params);
      final jobs = (response.data as List)
          .map((j) => JobModel.fromJson(j as Map<String, dynamic>))
          .toList();
      state = JobState(jobs: jobs);
    } catch (e) {
      state = JobState(error: e.toString());
    }
  }

  Future<void> fetchMyJobs() async {
    state = JobState(isLoading: true);
    try {
      final response = await apiService.get(ApiConfig.myJobs);
      final jobs = (response.data as List)
          .map((j) => JobModel.fromJson(j as Map<String, dynamic>))
          .toList();
      state = JobState(jobs: jobs);
    } catch (e) {
      state = JobState(error: e.toString());
    }
  }

  Future<void> createJob(Map<String, dynamic> jobData) async {
    try {
      await apiService.post(ApiConfig.jobs, data: jobData);
      await fetchMyJobs();
    } catch (e) {
      state = JobState(jobs: state.jobs, error: e.toString());
    }
  }
}

final jobProvider = StateNotifierProvider<JobNotifier, JobState>((ref) {
  return JobNotifier(ref.read(apiServiceProvider));
});
