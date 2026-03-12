class ReviewModel {
  final String id;
  final String bookingId;
  final String reviewerId;
  final String revieweeId;
  final int rating;
  final String? comment;
  final String? reviewerName;
  final String createdAt;

  ReviewModel({
    required this.id,
    required this.bookingId,
    required this.reviewerId,
    required this.revieweeId,
    required this.rating,
    this.comment,
    this.reviewerName,
    required this.createdAt,
  });

  factory ReviewModel.fromJson(Map<String, dynamic> json) => ReviewModel(
        id: json['id'] as String,
        bookingId: json['booking_id'] as String,
        reviewerId: json['reviewer_id'] as String,
        revieweeId: json['reviewee_id'] as String,
        rating: json['rating'] as int,
        comment: json['comment'] as String?,
        reviewerName: json['reviewer_name'] as String?,
        createdAt: json['created_at'] as String,
      );

  Map<String, dynamic> toJson() => {
        'id': id,
        'booking_id': bookingId,
        'reviewer_id': reviewerId,
        'reviewee_id': revieweeId,
        'rating': rating,
        'comment': comment,
        'reviewer_name': reviewerName,
        'created_at': createdAt,
      };
}
