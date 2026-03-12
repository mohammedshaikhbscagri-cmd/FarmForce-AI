import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/booking_model.dart';
import '../config/api_config.dart';
import 'auth_provider.dart';

class BookingState {
  final List<BookingModel> bookings;
  final bool isLoading;
  final String? error;

  BookingState({this.bookings = const [], this.isLoading = false, this.error});
}

class BookingNotifier extends StateNotifier<BookingState> {
  final apiService;

  BookingNotifier(this.apiService) : super(BookingState());

  Future<void> fetchBookings() async {
    state = BookingState(isLoading: true);
    try {
      final response = await apiService.get(ApiConfig.bookings);
      final bookings = (response.data as List)
          .map((b) => BookingModel.fromJson(b as Map<String, dynamic>))
          .toList();
      state = BookingState(bookings: bookings);
    } catch (e) {
      state = BookingState(error: e.toString());
    }
  }

  Future<void> acceptJob(String jobId, String workerId) async {
    try {
      await apiService.post(ApiConfig.bookings, data: {
        'job_id': jobId,
        'worker_id': workerId,
      });
      await fetchBookings();
    } catch (e) {
      state = BookingState(bookings: state.bookings, error: e.toString());
    }
  }

  Future<void> checkIn(String bookingId, double lat, double lng) async {
    try {
      await apiService.put('${ApiConfig.bookings}/$bookingId/check-in',
          data: {'latitude': lat, 'longitude': lng});
      await fetchBookings();
    } catch (e) {
      state = BookingState(bookings: state.bookings, error: e.toString());
    }
  }

  Future<void> checkOut(String bookingId) async {
    try {
      await apiService.put('${ApiConfig.bookings}/$bookingId/check-out');
      await fetchBookings();
    } catch (e) {
      state = BookingState(bookings: state.bookings, error: e.toString());
    }
  }
}

final bookingProvider = StateNotifierProvider<BookingNotifier, BookingState>((ref) {
  return BookingNotifier(ref.read(apiServiceProvider));
});
