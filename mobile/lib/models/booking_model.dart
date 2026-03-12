class BookingModel {
  final String id;
  final String jobId;
  final String workerId;
  final String status;
  final String? checkInTime;
  final String? checkOutTime;
  final double? checkInLat;
  final double? checkInLng;
  final bool farmerConfirmed;
  final String createdAt;

  BookingModel({
    required this.id,
    required this.jobId,
    required this.workerId,
    required this.status,
    this.checkInTime,
    this.checkOutTime,
    this.checkInLat,
    this.checkInLng,
    this.farmerConfirmed = false,
    required this.createdAt,
  });

  factory BookingModel.fromJson(Map<String, dynamic> json) => BookingModel(
        id: json['id'] as String,
        jobId: json['job_id'] as String,
        workerId: json['worker_id'] as String,
        status: json['status'] as String,
        checkInTime: json['check_in_time'] as String?,
        checkOutTime: json['check_out_time'] as String?,
        checkInLat: (json['check_in_lat'] as num?)?.toDouble(),
        checkInLng: (json['check_in_lng'] as num?)?.toDouble(),
        farmerConfirmed: (json['farmer_confirmed'] as bool?) ?? false,
        createdAt: json['created_at'] as String,
      );

  Map<String, dynamic> toJson() => {
        'id': id,
        'job_id': jobId,
        'worker_id': workerId,
        'status': status,
        'check_in_time': checkInTime,
        'check_out_time': checkOutTime,
        'check_in_lat': checkInLat,
        'check_in_lng': checkInLng,
        'farmer_confirmed': farmerConfirmed,
        'created_at': createdAt,
      };
}
