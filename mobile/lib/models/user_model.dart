class UserModel {
  final String id;
  final String phone;
  final String role;
  final String? name;
  final String? village;
  final String? district;
  final String? state;
  final String languagePref;
  final double avgRating;
  final int totalJobs;
  final bool isVerified;
  final String? profilePhotoUrl;
  final DateTime createdAt;

  UserModel({
    required this.id,
    required this.phone,
    required this.role,
    this.name,
    this.village,
    this.district,
    this.state,
    this.languagePref = 'hi',
    this.avgRating = 0.0,
    this.totalJobs = 0,
    this.isVerified = false,
    this.profilePhotoUrl,
    required this.createdAt,
  });

  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['id'] as String,
      phone: json['phone'] as String,
      role: json['role'] as String,
      name: json['name'] as String?,
      village: json['village'] as String?,
      district: json['district'] as String?,
      state: json['state'] as String?,
      languagePref: (json['language_pref'] as String?) ?? 'hi',
      avgRating: (json['avg_rating'] as num?)?.toDouble() ?? 0.0,
      totalJobs: (json['total_jobs'] as int?) ?? 0,
      isVerified: (json['is_verified'] as bool?) ?? false,
      profilePhotoUrl: json['profile_photo_url'] as String?,
      createdAt: DateTime.parse(json['created_at'] as String),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'phone': phone,
      'role': role,
      'name': name,
      'village': village,
      'district': district,
      'state': state,
      'language_pref': languagePref,
      'avg_rating': avgRating,
      'total_jobs': totalJobs,
      'is_verified': isVerified,
      'profile_photo_url': profilePhotoUrl,
      'created_at': createdAt.toIso8601String(),
    };
  }
}
