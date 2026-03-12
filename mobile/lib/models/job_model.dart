class JobModel {
  final String id;
  final String farmerId;
  final String taskType;
  final String cropType;
  final int workersNeeded;
  final double wagePerDay;
  final String startDate;
  final String endDate;
  final double locationLat;
  final double locationLng;
  final String village;
  final String district;
  final String state;
  final String status;
  final String urgency;
  final String? description;
  final String createdAt;

  JobModel({
    required this.id,
    required this.farmerId,
    required this.taskType,
    required this.cropType,
    required this.workersNeeded,
    required this.wagePerDay,
    required this.startDate,
    required this.endDate,
    required this.locationLat,
    required this.locationLng,
    required this.village,
    required this.district,
    required this.state,
    required this.status,
    required this.urgency,
    this.description,
    required this.createdAt,
  });

  factory JobModel.fromJson(Map<String, dynamic> json) {
    return JobModel(
      id: json['id'] as String,
      farmerId: json['farmer_id'] as String,
      taskType: json['task_type'] as String,
      cropType: json['crop_type'] as String,
      workersNeeded: json['workers_needed'] as int,
      wagePerDay: (json['wage_per_day'] as num).toDouble(),
      startDate: json['start_date'] as String,
      endDate: json['end_date'] as String,
      locationLat: (json['location_lat'] as num).toDouble(),
      locationLng: (json['location_lng'] as num).toDouble(),
      village: json['village'] as String,
      district: json['district'] as String,
      state: json['state'] as String,
      status: json['status'] as String,
      urgency: json['urgency'] as String,
      description: json['description'] as String?,
      createdAt: json['created_at'] as String,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'farmer_id': farmerId,
        'task_type': taskType,
        'crop_type': cropType,
        'workers_needed': workersNeeded,
        'wage_per_day': wagePerDay,
        'start_date': startDate,
        'end_date': endDate,
        'location_lat': locationLat,
        'location_lng': locationLng,
        'village': village,
        'district': district,
        'state': state,
        'status': status,
        'urgency': urgency,
        'description': description,
        'created_at': createdAt,
      };
}
