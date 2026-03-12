import 'package:geolocator/geolocator.dart';
import 'dart:math';

class LocationService {
  Future<Position> getCurrentLocation() async {
    bool serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) {
      throw Exception('Location services are disabled.');
    }

    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        throw Exception('Location permissions are denied');
      }
    }

    if (permission == LocationPermission.deniedForever) {
      throw Exception('Location permissions are permanently denied');
    }

    return Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high);
  }

  /// Check if the user is within radius_meters of (centerLat, centerLng).
  bool checkInAtField(double lat, double lng, double centerLat, double centerLng,
      {double radiusMeters = 100}) {
    const double earthRadius = 6371000;
    final double dLat = _toRad(lat - centerLat);
    final double dLng = _toRad(lng - centerLng);
    final double a = sin(dLat / 2) * sin(dLat / 2) +
        cos(_toRad(centerLat)) *
            cos(_toRad(lat)) *
            sin(dLng / 2) *
            sin(dLng / 2);
    final double distance = earthRadius * 2 * atan2(sqrt(a), sqrt(1 - a));
    return distance <= radiusMeters;
  }

  double _toRad(double deg) => deg * (pi / 180);
}
