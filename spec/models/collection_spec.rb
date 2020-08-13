require 'rails_helper'

RSpec.describe Collection, type: :model do
  describe 'associations' do
    it { should have_many(:skins) }
  end

  describe 'validations' do
    it { should validate_presence_of(:name) }
    it { should validate_presence_of(:category) }
  end
end
