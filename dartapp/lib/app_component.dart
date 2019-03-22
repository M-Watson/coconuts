import 'package:angular/angular.dart';
import 'src/hero.dart';
import 'src/mock_heros.dart';
import 'package:angular_forms/angular_forms.dart';

@Component(
  selector: 'my-app',
  // ...

  templateUrl: 'app_component.html',

  directives: [coreDirectives, formDirectives],
)

class AppComponent {
  final title = 'Tour';
  List<Hero> heros = mockHeros;
}
