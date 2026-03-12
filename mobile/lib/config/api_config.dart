class ApiConfig {
  static const String baseUrl = 'http://localhost:8000/api/v1';

  // Auth
  static const String sendOtp = '/auth/send-otp';
  static const String verifyOtp = '/auth/verify-otp';
  static const String refreshToken = '/auth/refresh-token';

  // Users
  static const String me = '/users/me';
  static const String myFarm = '/users/me/farm';
  static const String mySkills = '/users/me/skills';

  // Jobs
  static const String jobs = '/jobs';
  static const String myJobs = '/jobs/my-jobs';
  static const String voiceJob = '/jobs/voice';

  // Bookings
  static const String bookings = '/bookings';

  // Payments
  static const String createOrder = '/payments/create-order';
  static const String verifyPayment = '/payments/verify';
  static const String paymentHistory = '/payments/history';

  // Reviews
  static const String reviews = '/reviews';

  // Matching
  static const String matchWorkers = '/matching/workers';
  static const String matchJobs = '/matching/jobs';

  // Services
  static const String nearbyServices = '/services/nearby';

  // Predictions
  static const String laborDemand = '/predictions/labor-demand';
  static const String wageSuggestion = '/predictions/wage-suggestion';
}
