import 'package:go_router/go_router.dart';
import '../screens/splash_screen.dart';
import '../screens/onboarding/language_selection_screen.dart';
import '../screens/onboarding/phone_login_screen.dart';
import '../screens/onboarding/otp_verification_screen.dart';
import '../screens/onboarding/role_selection_screen.dart';
import '../screens/onboarding/profile_setup_screen.dart';
import '../screens/farmer/farmer_home_screen.dart';
import '../screens/farmer/post_job_screen.dart';
import '../screens/farmer/worker_discovery_screen.dart';
import '../screens/farmer/job_detail_screen.dart';
import '../screens/farmer/booking_management_screen.dart';
import '../screens/farmer/payment_screen.dart';
import '../screens/farmer/farmer_profile_screen.dart';
import '../screens/worker/worker_home_screen.dart';
import '../screens/worker/job_search_screen.dart';
import '../screens/worker/job_detail_screen.dart';
import '../screens/worker/my_bookings_screen.dart';
import '../screens/worker/earnings_screen.dart';
import '../screens/worker/check_in_screen.dart';
import '../screens/worker/worker_profile_screen.dart';
import '../screens/common/map_screen.dart';
import '../screens/common/chat_screen.dart';
import '../screens/common/notifications_screen.dart';
import '../screens/common/settings_screen.dart';

final appRouter = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(path: '/', builder: (context, state) => const SplashScreen()),
    GoRoute(path: '/language', builder: (context, state) => const LanguageSelectionScreen()),
    GoRoute(path: '/login', builder: (context, state) => const PhoneLoginScreen()),
    GoRoute(path: '/otp', builder: (context, state) => const OtpVerificationScreen()),
    GoRoute(path: '/role', builder: (context, state) => const RoleSelectionScreen()),
    GoRoute(path: '/profile-setup', builder: (context, state) => const ProfileSetupScreen()),
    // Farmer routes
    GoRoute(path: '/farmer/home', builder: (context, state) => const FarmerHomeScreen()),
    GoRoute(path: '/farmer/post-job', builder: (context, state) => const PostJobScreen()),
    GoRoute(path: '/farmer/workers', builder: (context, state) => const WorkerDiscoveryScreen()),
    GoRoute(path: '/farmer/job/:id', builder: (context, state) => const FarmerJobDetailScreen()),
    GoRoute(path: '/farmer/bookings', builder: (context, state) => const BookingManagementScreen()),
    GoRoute(path: '/farmer/payment', builder: (context, state) => const PaymentScreen()),
    GoRoute(path: '/farmer/profile', builder: (context, state) => const FarmerProfileScreen()),
    // Worker routes
    GoRoute(path: '/worker/home', builder: (context, state) => const WorkerHomeScreen()),
    GoRoute(path: '/worker/search', builder: (context, state) => const JobSearchScreen()),
    GoRoute(path: '/worker/job/:id', builder: (context, state) => const WorkerJobDetailScreen()),
    GoRoute(path: '/worker/bookings', builder: (context, state) => const MyBookingsScreen()),
    GoRoute(path: '/worker/earnings', builder: (context, state) => const EarningsScreen()),
    GoRoute(path: '/worker/check-in', builder: (context, state) => const CheckInScreen()),
    GoRoute(path: '/worker/profile', builder: (context, state) => const WorkerProfileScreen()),
    // Common routes
    GoRoute(path: '/map', builder: (context, state) => const MapScreen()),
    GoRoute(path: '/chat', builder: (context, state) => const ChatScreen()),
    GoRoute(path: '/notifications', builder: (context, state) => const NotificationsScreen()),
    GoRoute(path: '/settings', builder: (context, state) => const SettingsScreen()),
  ],
);
