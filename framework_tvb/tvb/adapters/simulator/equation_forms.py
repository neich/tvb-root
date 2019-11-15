from tvb.datatypes.equations import Equation, Linear, Gaussian, DoubleGaussian, Sigmoid, GeneralizedSigmoid, Sinusoid, \
    Cosine, Alpha, PulseTrain, Gamma, DoubleExponential, FirstOrderVolterra, MixtureOfGammas

from tvb.core.neotraits.forms import Form, ScalarField, SimpleFloatField


LINEAR_EQUATION = 'Linear'
GAUSSIAN_EQUATION = 'Gaussian'
DOUBLE_GAUSSIAN_EQUATION = 'DoubleGaussian'
SIGMOID_EQUATION = 'Sigmoid'
GENRALIZED_SIGMOID_EQUATION = 'GeneralizedSigmoid'
SINUSOID_EQUATION = 'Sinusoid'
COSINE_EQUATION = 'Cosine'
ALPHA_EQUATION = 'Alpha'
PULSE_TRAIN_EQUATION = 'PulseTrain'


def get_ui_name_to_equation_dict():
    eq_name_to_class = {
        LINEAR_EQUATION: Linear,
        GAUSSIAN_EQUATION: Gaussian,
        DOUBLE_GAUSSIAN_EQUATION: DoubleGaussian,
        SIGMOID_EQUATION: Sigmoid,
        GENRALIZED_SIGMOID_EQUATION: GeneralizedSigmoid,
        SINUSOID_EQUATION: Sinusoid,
        COSINE_EQUATION: Cosine,
        ALPHA_EQUATION: Alpha,
        PULSE_TRAIN_EQUATION: PulseTrain
    }
    return eq_name_to_class


def get_ui_name_for_equation(equation_class):
    equation_to_ui_name = dict((v, k) for k, v in get_ui_name_to_equation_dict().items())
    return equation_to_ui_name.get(equation_class)


def get_ui_name_to_monitor_equation_dict():
    eq_name_to_class = {
        'HRF kernel: Gamma kernel': Gamma,
        'HRF kernel: Difference of Exponentials': DoubleExponential,
        'HRF kernel: Volterra Kernel': FirstOrderVolterra,
        'HRF kernel: Mixture of Gammas': MixtureOfGammas
    }
    return eq_name_to_class


def get_equation_to_form_dict():
    coupling_class_to_form = {
        Linear: LinearEquationForm,
        Gaussian: GaussianEquationForm,
        DoubleGaussian: DoubleGaussianEquationForm,
        Sigmoid: SigmoidEquationForm,
        GeneralizedSigmoid: GeneralizedSigmoidEquationForm,
        Sinusoid: SinusoidEquationForm,
        Cosine: CosineEquationForm,
        Alpha: AlphaEquationForm,
        PulseTrain: PulseTrainEquationForm,
        Gamma: GammaEquationForm,
        DoubleExponential: DoubleExponentialEquationForm,
        FirstOrderVolterra: FirstOrderVolterraEquationForm,
        MixtureOfGammas: MixtureOfGammasEquationForm
    }

    return coupling_class_to_form


def get_form_for_equation(equation_class):
    return get_equation_to_form_dict().get(equation_class)


class EquationForm(Form):

    def get_traited_equation(self):
        return Equation

    def __init__(self, prefix=''):
        super(EquationForm, self).__init__(prefix)
        self.equation = ScalarField(self.get_traited_equation().equation, self, disabled=True)
        for param_key, param in self.get_traited_equation().parameters.default().items():
            setattr(self, param_key, SimpleFloatField(self, param_key, required=True, label=param_key, default=param))


class LinearEquationForm(EquationForm):

    def get_traited_equation(self):
        return Linear

    def __init__(self, prefix=''):
        super(LinearEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['a'] = self.a.data
        datatype.parameters['b'] = self.b.data

    def fill_from_trait(self, trait):
        self.a.data = trait.parameters['a']
        self.b.data = trait.parameters['b']

class GaussianEquationForm(EquationForm):

    def get_traited_equation(self):
        return Gaussian

    def __init__(self, prefix=''):
        super(GaussianEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['amp'] = self.amp.data
        datatype.parameters['sigma'] = self.sigma.data
        datatype.parameters['midpoint'] = self.midpoint.data
        datatype.parameters['offset'] = self.offset.data

    def fill_from_trait(self, trait):
        self.amp.data = trait.parameters['amp']
        self.sigma.data = trait.parameters['sigma']
        self.midpoint.data = trait.parameters['midpoint']
        self.offset.data = trait.parameters['offset']


class DoubleGaussianEquationForm(EquationForm):

    def get_traited_equation(self):
        return DoubleGaussian

    def __init__(self, prefix=''):
        super(DoubleGaussianEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['amp_1'] = self.amp_1.data
        datatype.parameters['amp_2'] = self.amp_2.data
        datatype.parameters['sigma_1'] = self.sigma_1.data
        datatype.parameters['sigma_2'] = self.sigma_2.data
        datatype.parameters['midpoint_1'] = self.midpoint_1.data
        datatype.parameters['midpoint_2'] = self.midpoint_2.data

    def fill_from_trait(self, trait):
        self.amp_1.data = trait.parameters['amp_1']
        self.amp_2.data = trait.parameters['amp_2']
        self.sigma_1.data = trait.parameters['sigma_1']
        self.sigma_2.data = trait.parameters['sigma_2']
        self.midpoint_1.data = trait.parameters['midpoint_1']
        self.midpoint_2.data = trait.parameters['midpoint_2']


class SigmoidEquationForm(EquationForm):

    def get_traited_equation(self):
        return Sigmoid

    def __init__(self, prefix=''):
        super(SigmoidEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['amp'] = self.amp.data
        datatype.parameters['radius'] = self.radius.data
        datatype.parameters['sigma'] = self.sigma.data
        datatype.parameters['offset'] = self.offset.data

    def fill_from_trait(self, trait):
        self.amp.data = trait.parameters['amp']
        self.radius.data = trait.parameters['radius']
        self.sigma.data = trait.parameters['sigma']
        self.offset.data = trait.parameters['offset']


class GeneralizedSigmoidEquationForm(EquationForm):

    def get_traited_equation(self):
        return GeneralizedSigmoid

    def __init__(self, prefix=''):
        super(GeneralizedSigmoidEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['low'] = self.low.data
        datatype.parameters['high'] = self.high.data
        datatype.parameters['midpoint'] = self.midpoint.data
        datatype.parameters['sigma'] = self.sigma.data

    def fill_from_trait(self, trait):
        self.low.data = trait.parameters['low']
        self.high.data = trait.parameters['high']
        self.midpoint.data = trait.parameters['midpoint']
        self.sigma.data = trait.parameters['sigma']


class SinusoidEquationForm(EquationForm):

    def get_traited_equation(self):
        return Sinusoid

    def __init__(self, prefix=''):
        super(SinusoidEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['amp'] = self.amp.data
        datatype.parameters['frequency'] = self.frequency.data

    def fill_from_trait(self, trait):
        self.amp.data = trait.parameters['amp']
        self.frequency.data = trait.parameters['frequency']


class CosineEquationForm(EquationForm):

    def get_traited_equation(self):
        return Cosine

    def __init__(self, prefix=''):
        super(CosineEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['amp'] = self.amp.data
        datatype.parameters['frequency'] = self.frequency.data

    def fill_from_trait(self, trait):
        self.amp.data = trait.parameters['amp']
        self.frequency.data = trait.parameters['frequency']


class AlphaEquationForm(EquationForm):

    def get_traited_equation(self):
        return Alpha

    def __init__(self, prefix=''):
        super(AlphaEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['onset'] = self.onset.data
        datatype.parameters['alpha'] = self.alpha.data
        datatype.parameters['beta'] = self.beta.data

    def fill_from_trait(self, trait):
        self.onset.data = trait.parameters['onset']
        self.alpha.data = trait.parameters['alpha']
        self.beta.data = trait.parameters['beta']


class PulseTrainEquationForm(EquationForm):

    def get_traited_equation(self):
        return PulseTrain

    def __init__(self, prefix=''):
        super(PulseTrainEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['T'] = self.T.data
        datatype.parameters['tau'] = self.tau.data
        datatype.parameters['amp'] = self.amp.data
        datatype.parameters['onset'] = self.onset.data

    def fill_from_trait(self, trait):
        self.T.data = trait.parameters['T']
        self.tau.data = trait.parameters['tau']
        self.amp.data = trait.parameters['amp']
        self.onset.data = trait.parameters['onset']


class GammaEquationForm(EquationForm):

    def get_traited_equation(self):
        return Gamma

    def __init__(self, prefix=''):
        super(GammaEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['tau'] = self.tau.data
        datatype.parameters['n'] = self.n.data
        datatype.parameters['factorial'] = self.factorial.data
        datatype.parameters['a'] = self.a.data

    def fill_from_trait(self, trait):
        self.tau.data = trait.parameters['tau']
        self.n.data = trait.parameters['n']
        self.factorial.data = trait.parameters['factorial']
        self.a.data = trait.parameters['a']


class DoubleExponentialEquationForm(EquationForm):

    def get_traited_equation(self):
        return DoubleExponential

    def __init__(self, prefix=''):
        super(DoubleExponentialEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['tau_1'] = self.tau_1.data
        datatype.parameters['tau_2'] = self.tau_2.data
        datatype.parameters['a'] = self.a.data
        datatype.parameters['f_1'] = self.f_1.data
        datatype.parameters['f_2'] = self.f_2.data
        datatype.parameters['pi'] = self.pi.data
        datatype.parameters['amp_1'] = self.amp_1.data
        datatype.parameters['amp_2'] = self.amp_2.data

    def fill_from_trait(self, trait):
        self.tau_1.data = trait.parameters['tau_1']
        self.tau_2.data = trait.parameters['tau_2']
        self.a.data = trait.parameters['a']
        self.f_1.data = trait.parameters['f_1']
        self.f_2.data = trait.parameters['f_2']
        self.pi.data = trait.parameters['pi']
        self.amp_1.data = trait.parameters['amp_1']
        self.amp_2.data = trait.parameters['amp_2']


class FirstOrderVolterraEquationForm(EquationForm):

    def get_traited_equation(self):
        return FirstOrderVolterra

    def __init__(self, prefix=''):
        super(FirstOrderVolterraEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['tau_s'] = self.tau_s.data
        datatype.parameters['tau_f'] = self.tau_f.data
        datatype.parameters['k_1'] = self.k_1.data
        datatype.parameters['V_0'] = self.V_0.data

    def fill_from_trait(self, trait):
        self.tau_s.data = trait.parameters['tau_s']
        self.tau_f.data = trait.parameters['tau_f']
        self.k_1.data = trait.parameters['k_1']
        self.V_0.data = trait.parameters['V_0']


class MixtureOfGammasEquationForm(EquationForm):

    def get_traited_equation(self):
        return MixtureOfGammas

    def __init__(self, prefix=''):
        super(MixtureOfGammasEquationForm, self).__init__(prefix)

    def fill_trait(self, datatype):
        datatype.parameters['a_1'] = self.a_1.data
        datatype.parameters['a_2'] = self.a_2.data
        datatype.parameters['l'] = self.l.data
        datatype.parameters['c'] = self.c.data
        datatype.parameters['gamma_a_1'] = self.gamma_a_1.data
        datatype.parameters['gamma_a_2'] = self.gamma_a_2.data

    def fill_from_trait(self, trait):
        self.a_1.data = trait.parameters['a_1']
        self.a_2.data = trait.parameters['a_2']
        self.l.data = trait.parameters['l']
        self.c.data = trait.parameters['c']
        self.gamma_a_1.data = trait.parameters['gamma_a_1']
        self.gamma_a_2.data = trait.parameters['gamma_a_2']