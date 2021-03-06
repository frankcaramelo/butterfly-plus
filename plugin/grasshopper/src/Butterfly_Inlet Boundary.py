# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create an inlet boundary with uniform velocity value.

-

    Args:
        _velocityVec: Velocity vector.
        temperature_: Temperature in degrees celsius.
    Returns:
        inletBoundary: Buttefly inlet boundary.
"""

ghenv.Component.Name = "Butterfly_Inlet Boundary"
ghenv.Component.NickName = "inletvel"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "01::Boundary"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly import boundarycondition as bc
    from butterfly.fields import FixedValue
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _velocityVec:
    _velocityVec = FixedValue(str((_velocityVec.X, _velocityVec.Y, _velocityVec.Z)).replace(',', '')) \
                   if _velocityVec \
                   else None

    temperature_ = FixedValue(str(temperature_ + 273.15)) \
                   if temperature_ \
                   else None
                   
    inletBoundary = bc.FixedInletBoundaryCondition(U=_velocityVec,
                                                   T = temperature_)

