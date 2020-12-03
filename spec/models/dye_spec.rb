require 'rails_helper'

RSpec.describe Dye, type: :model do
  it { should serialize(:base_rgb) }

  describe 'validations' do
    it { should validate_presence_of(:api_id) }
  end
end
